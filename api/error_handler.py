''' Override standard error management to return json instead of html'''
from flask import make_response, jsonify
from . import app

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

@app.errorhandler(500)
def internl_eror(error):
    return make_response(jsonify({'error': 'Server internal error'}), 500)