import errno
import requests
from http.client import BadStatusLine
from requests import exceptions as requests_exceptions
from retrying import retry


def retry_request(exception):
    """
    We try again if one of these exceptions happen. 
    """
    return not ((
        not isinstance(exception, requests_exceptions.ConnectionError)
        and not isinstance(exception, requests_exceptions.ConnectTimeout))
        and not isinstance(exception, BadStatusLine or exception.errno == errno.ECONNRESET
    ))


@retry(retry_on_exception=retry_request, wait_fixed=3000)
def action_request(method, url, data=None, headers=None):
    """
    Action the request with the specific method
    """
    try:
        if method == 'GET':
            resp = requests.get(url, headers=headers)
            return resp
        elif method == 'POST':
            resp = requests.post(url, json=data, headers=headers)
            return resp
    except (Exception, e):
        print('Retry {0} with {1}, {2}'.format(str(e), url, data))
        raise e
