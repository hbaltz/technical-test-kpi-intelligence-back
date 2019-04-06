""" Manages the response """
from flask import make_response

JSON_MIME_TYPE = 'application/json'

def json_response(data='', status=200, headers=None):
    """ Description
    :type data: JSON
    :param data: The data to insert in the response

    :type status: Integer
    :param status: The status of the response

    :type headers: Array
    :param headers: The headers of the response

    :raises:

    :rtype:
    """
    headers = headers or {}
    if 'Content-Type' not in headers:
        headers['Content-Type'] = JSON_MIME_TYPE
    return make_response(data, status, headers)