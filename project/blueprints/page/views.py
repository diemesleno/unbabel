from flask import render_template, redirect, url_for, request
from flask.views import MethodView
from sqlalchemy.sql.expression import func

from project.blueprints.page.models import Translate
from project.blueprints.page.forms import TranslateForm

# from flask import Blueprint

# page = Blueprint('page', __name__, template_folder='templates') #create the templates folder inside the page folder

"""
@page.route('/')
def home():
    return render_template('page/home.html')
"""


class PageView(MethodView):
    def get(self):
        form = TranslateForm()
        translates = Translate.query.order_by(func.length(Translate.translated_text)).all()
        return render_template('page.html', translates=translates, form=form)
    
    def post(self):
        form = TranslateForm()
        if form.validate_on_submit():
            # It prevents circular imports
            from project.blueprints.page.tasks import ask_translation
            ask_translation.delay(request.form.get('input_text'))
        return redirect(url_for('page'))

