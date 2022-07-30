from flask import Flask, Response, request, jsonify
from flask_cors import CORS
from controller.series_controller import serie_controller_post
from controller.series_controller import serie_controller_get
from controller.series_controller import id_controller_get
from controller.series_controller import id_controller_delete
from commons.utils import default_error
import json

app = Flask(__name__)
CORS(app)


def body_response(body={}, status=200):
    return Response(
        json.dumps(body, default=str),
        mimetype="application/json",
        status=status
    )


@app.route('/')
def home_page():
    return jsonify(hello='world')


@app.route('/serie', methods=['GET'])
def series():
    app.logger.info('Method series init')
    message = serie_controller_get()
    result = body_response(message, 200)
    app.logger.info('Method series ending')
    return result


@app.route('/serie', methods=['POST'])
def series_create():
    app.logger.info('Method series_create init')
    body = dict(request.json)
    message, status_code = serie_controller_post(body)
    result = body_response(message, status_code)
    app.logger.info('Method series_create ending')
    return result


@app.route('/serie/<serie_id>', methods=['GET'])
def get_serie_id(serie_id):
    app.logger.info('Method get_serie_id init')
    app.logger.info(f'Path param: {serie_id}')
    message, status_code = id_controller_get(serie_id)
    result = body_response(message, status_code)
    app.logger.info('Method get_serie_id ending')
    return result


@app.route('/serie/<serie_id>', methods=['DELETE'])
def delete_serie_id(serie_id):
    app.logger.info('Method delete_serie_id init')
    app.logger.info(f'Path param: {serie_id}')
    message, status_code = id_controller_delete(serie_id)
    result = body_response(message, status_code)
    app.logger.info('Method delete_serie_id ending')
    return result


@app.errorhandler(404)
def not_found(error=None):
    app.logger.info('Error: not_found')
    message = default_error(request.url, error)
    app.logger.error(message)
    result = body_response(message, 404)
    return result


@app.errorhandler(405)
def method_not_allowed(error=None):
    app.logger.info('Error: method_not_allowed')
    message = default_error(request.url, error)
    app.logger.error(message)
    result = body_response(message, 405)
    return result


@app.errorhandler(400)
def method_bat_request(error=None):
    app.logger.info('Error: method_bat_request')
    message = default_error(request.url, error)
    app.logger.error(message)
    result = body_response(message, 400)
    return result
