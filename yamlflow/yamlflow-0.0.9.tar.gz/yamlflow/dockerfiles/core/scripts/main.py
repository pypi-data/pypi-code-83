import logging

from flask import (
    Flask, 
    request,
    jsonify)

from service.config import config
from service.predictor import Predictor


predictor = Predictor(**config)
app = Flask(__name__)

gunicorn_logger = logging.getLogger('gunicorn.error')
app.logger.handlers = gunicorn_logger.handlers
app.logger.setLevel(gunicorn_logger.level)


@app.route('/', methods=['POST'])
def predict():
    payload = request.json
    if not payload:
        #TODO: log error
        return jsonify({"error": "Payload is empty."}), 400
    app.logger.info(f"requst_body: {payload}")
    try:
        response = predictor.predict(payload)
    except Exception as err:
        return jsonify({"error": "Bad request error"}), 400
    app.logger.info(f"respone_body: {response}")
    return jsonify(response), 200


@app.route('/healthcheck', methods=['GET'])
def healthcheck():
    #TODO: is healtcheck mandatory?
    if predictor.healthcheck():
        return {"True", "ok"}
    return {"False", "fail"}
