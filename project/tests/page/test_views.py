from flask import url_for


class TestPage(object):
    def test_get_home_page(self, client):
        """
        Home page should respond with a success 200 on the GET method.
        """
        response = client.get(url_for('page'))
        assert response.status_code == 200
