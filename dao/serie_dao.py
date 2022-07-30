import os
import traceback
from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config['MONGO_URI'] = os.environ.get('MONGO_URI')
app.logger.info('Try to connect to the database')
try:
    app.logger.info('Connected correctly')
    mongo = PyMongo(app)
    collection = mongo.db.registries
except Exception:
    traceback.print_exc()


def insert_one(propertys):
    app.logger.info('Method insert_one init')
    app.logger.info(f'propertys: {propertys}')
    operation = collection.insert_one(propertys)
    identification = operation.inserted_id
    app.logger.info(f'Result insert: {identification}')
    app.logger.info('Method insert_one ending')
    return identification


def find():
    app.logger.info('Method find init')
    result_operation = list(collection.find())
    size = len(result_operation)
    app.logger.info(f'Result search: {result_operation}')
    app.logger.info(f'Count find: {size}')
    app.logger.info('Method find ending')
    return result_operation, size


def find_id(serie_id):
    app.logger.info('Method find_id init')
    result = list(collection.find(serie_id))
    app.logger.info(f'Result search: {result}')
    app.logger.info('Method find_id ending')
    return result


def delete_one(note_id):
    app.logger.info('Method delete_one init')
    result_operation = collection.delete_one(note_id)
    app.logger.info(result_operation.raw_result)
    app.logger.info('Method delete_one ending')
    return result_operation.raw_result
