import logging
from flask import Flask, abort, json, request
from . import app, error_handler
from .utils import loader, response


@app.route("/api/investment", methods=['GET'])
def get_data():
    city = request.args.get('city', None)
    progress_status = request.args.get('progress_status', None)

    # We recover the investment data
    try:
        json_data = loader.getStaticData("data.json")
    except FileNotFoundError as identifier:
        logging.exception(identifier)
        abort(500)

    # If a city was passed in argument, we applied the filter on 'ville'
    if city:
        json_data = [
            json_data for json_data in json_data if json_data['ville'] == city]

    # If a porgess status was passed in argument, we applied the filter on 'etat_d_avancement'
    if progress_status:
        json_data = [
            json_data for json_data in json_data if json_data['etat_d_avancement'] == progress_status]

    result = response.json_response(json.dumps(json_data))

    return result