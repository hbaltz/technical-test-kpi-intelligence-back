from flask import Flask, abort, json, request
from sqlalchemy import and_
from . import app, error_handler, models, db
from .utils import loader, response, alchemy_json_encoder


@app.route("/api/investment", methods=['GET'])
def get_data():
    """ Get the investment data depending on the paramter passed to the request 
    :raises:

    :rtype:
    """
    city = request.args.get('city', None)
    progress_status = request.args.get('progress_status', None)

    filters = []

    # We recover the investment data depending on the filter
    if city and progress_status:
        investments = models.Investment.query.filter(and_(models.Investment.ville==city, models.Investment.etat_d_avancement==progress_status)).all()
    elif city:
        investments = models.Investment.query.filter(models.Investment.ville==city).all()
    elif progress_status: 
        investments = models.Investment.query.filter(models.Investment.etat_d_avancement==progress_status).all()
    else: 
        investments = models.Investment.query.all()

    result = response.json_response(json.dumps(investments, cls=alchemy_json_encoder.AlchemyEncoder))

    return result


@app.route("/api/investment/<int:investment_id>", methods=['GET'])
def get_investment_by_id(investment_id):
    """ Recover a investment using his id
    :type investment_id: String
    :param investment_id: The investment's id

    :raises:

    :rtype:
    """
    invest = models.Investment.query.get(investment_id)
    if not invest:
        abort(404)
    result = response.json_response(json.dumps(invest, cls=alchemy_json_encoder.AlchemyEncoder))
    return result
