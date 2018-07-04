from flask import url_for


class TestPage(object):
    def test_get_home_page(self, client):
        """
        Home page should respond with a success 200 on the GET method.
        """
        response = client.get(url_for('page'))
        assert response.status_code == 200
    
    #def test_post_form_home_page(self, client):
    #    """ 
    #    Home page should respond with a success 200 on the POST method.
    #    """
    #    form = {
    #        'input_text': 'There is a house in New Orleans...'
    #    }
    #    response = client.post(url_for('page'), data=form, follow_redirects=True)
    #    assert response.status_code == 200
    #