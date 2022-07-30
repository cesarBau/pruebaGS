from flask import Flask
from bson.objectid import ObjectId
from bson.errors import InvalidId
from services.serie_service import serie_service_post
from services.serie_service import serie_service_get
from services.serie_service import serie_id_service_get
from services.serie_service import serie_id_service_delete
from commons.utils import default_error


app = Flask(__name__)
URL = 'http://localhost:5000'
message = ''
status_code = 0

def serie_controller_get():
    app.logger.info('Method serie_controller_get init')
    process, size = serie_service_get()
    result = {
        'length': size,
        'result': process
    }
    app.logger.info('Method serie_controller_get ending')
    return result


def serie_controller_post(body):
    app.logger.info('Method serie_controller_post init')
    app.logger.info(f'Petition body : {body}')
    status_code = 400
    if('limit' not in body):
        message = default_error(f'{URL}/serie','the limit field is required')
    elif(body['limit'] < 2):
        message = default_error(f'{URL}/serie','the limit field must be greater than 1')
    else: 
        identification, limit, fibonacci = serie_service_post(body['limit'])
        message = {
            '_id': identification,
            'size': limit,
            'data': fibonacci
        }
        status_code = 200
    app.logger.info('Method serie_controller_post ending')
    return message, status_code


def id_controller_get(serie_id):
    app.logger.info('Method id_controller_get init')
    app.logger.info(f'serie_id: {serie_id}')
    try:
        validation = ObjectId(serie_id)
        app.logger.info(validation)
        process = serie_id_service_get(serie_id)
        message = {
            'result': process
        }
        status_code = 200
    except InvalidId:
        message = default_error(f'{URL}/serie/{serie_id}','format id invalid')
        status_code = 400
    app.logger.info('Method id_controller_get ending')
    return message, status_code


def id_controller_delete(serie_id):
    app.logger.info('Method id_controller_delete init')
    app.logger.info(f'Path param : {serie_id}')
    try: 
        validation = ObjectId(serie_id)
        app.logger.info(validation)
        message = serie_id_service_delete(serie_id)
        status_code = 204
    except InvalidId:
        message = default_error(f'{URL}/serie/{serie_id}','format id invalid')
        status_code = 400
    app.logger.info('Method id_controller_delete ending')
    return message, status_code
