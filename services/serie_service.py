from flask import Flask
from bson.objectid import ObjectId
from dao.serie_dao import insert_one
from dao.serie_dao import find
from dao.serie_dao import find_id
from dao.serie_dao import delete_one
from commons.utils import fib
from commons.utils import file_data
from commons.utils import file_delete

app = Flask(__name__)


def serie_service_get():
    app.logger.info('Method serie_service_get init')
    result, size = find()
    app.logger.info('Method serie_service_get ending')
    return result, size


def serie_service_post(limit):
    app.logger.info('Method serie_service_post init')
    app.logger.info(f'Limit: {limit}')
    fibonacci = fib(limit)
    data = {'size': limit, 'data': fibonacci}
    identification = insert_one(data)
    app.logger.info(f'Result service: {identification}')
    write_file = f'_id:{identification}|size:{limit}|data:{fibonacci}'
    app.logger.info(f'write_file: {write_file}')
    file_data(write_file)
    app.logger.info('Method serie_service_post ending')
    return identification, limit, fibonacci


def serie_id_service_get(serie_id):
    app.logger.info('Method serie_id_service_get init')
    search = {'_id': ObjectId(serie_id)}
    app.logger.info(f'search: {search}')
    result = find_id(search)
    app.logger.info('Method serie_id_service_get ending')
    return result


def serie_id_service_delete(serie_id):
    app.logger.info('Method serie_id_service_delete init')
    delete = {'_id': ObjectId(serie_id)}
    app.logger.info(f'delete: {delete}')
    result = delete_one(delete)
    file_delete(serie_id)
    app.logger.info('Method serie_id_service_delete ending')
    return result
