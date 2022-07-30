from flask import Flask
from services.serie_service import serie_service_post
from services.serie_service import serie_service_get
from services.serie_service import serie_id_service_get
from services.serie_service import serie_id_service_delete

app = Flask(__name__)


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
    identification, limit, fibonacci = serie_service_post(body['limit'])
    result = {
        '_id': identification,
        'size': limit,
        'data': fibonacci
    }
    app.logger.info('Method serie_controller_post ending')
    return result


def id_controller_get(serie_id):
    app.logger.info('Method id_controller_get init')
    app.logger.info(f'serie_id: {serie_id}')
    process = serie_id_service_get(serie_id)
    result = {
        'result': process
    }
    app.logger.info('Method id_controller_get ending')
    return result


def id_controller_delete(serie_id):
    app.logger.info('Method id_controller_delete init')
    app.logger.info(f'Path param : {serie_id}')
    result = serie_id_service_delete(serie_id)
    app.logger.info('Method id_controller_delete ending')
    return result
