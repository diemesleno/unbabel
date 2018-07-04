from project.app import create_celery_app
from project.blueprints.page.models import Translate
from lib.util_request import action_request
from config.settings import UNBABEL_URL, HEADERS

from celery.schedules import crontab
from celery.task import periodic_task

celery = create_celery_app()


@celery.task(name='unbabel.add_database')
def add_database(uid, text, order_number, status):
    """
    Create the Translate object and save on database.

    :param uid: UID from the text
    :param text: Text to translate
    :param order_number: The order_number to translate
    :param status: The status from translation process
    :return: None
    """
    translate = Translate(
                    uid=uid, 
                    original_text=text, 
                    translated_text='Translating', 
                    order_number=int(order_number), 
                    status=status
                )
    translate.save()
    return None

@celery.task(name='unbabel.ask_translation')
def ask_translation(original_text):
    """
    Ask the Unbabel API to translate a text and return the response.

    :param original_text: The input_text to translate
    :return: None
    """
    send_data = {
        "text": original_text,
        "source_language": "en",
        "target_language": "es",
        "text_format": "text" 
    }
    resp = action_request(method='POST', url=UNBABEL_URL, data=send_data, headers=HEADERS)
    if resp.status_code == 201:
        ret_data = resp.json()
        add_database.delay(uid=ret_data['uid'], text=ret_data['text'], order_number=ret_data['order_number'], status=ret_data['status'])
    return None



@celery.task(name='unbabel.update_database')
def update_database(uid, translated_text, status):
    translated = Translate.query.filter_by(uid=uid).first()
    if translated:
        translated.translated_text = translated_text
        translated.status = status
        translated.update()
    return None


#@periodic_task(run_every=crontab(minute='*/1'))
@celery.task(name='unbabel.get_translateds')
def get_translateds():
    """ 
    Get the translated texts yet not proccessed and check the translation proccess

    :return: None
    """
    translates = Translate.query.filter(Translate.status != 'completed').all()
    for t in translates:
        GET_UNBABEL_URL = '{0}{1}/'.format(UNBABEL_URL, t.uid)
        resp = action_request(method='GET', url=GET_UNBABEL_URL, headers=HEADERS)
        if resp.status_code == 200:
            ret_data = resp.json()
            if ret_data['status'] == 'completed':
                update_database.delay(uid=ret_data['uid'], translated_text=ret_data['translatedText'], status=ret_data['status'])
            else:
                update_database.delay(uid=ret_data['uid'], translated_text='Translating', status=ret_data['status'])
    return None
