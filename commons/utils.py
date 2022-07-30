from flask import Flask
from functools import reduce
import codecs

app = Flask(__name__)


def default_error(url, error):
    return {
        'url': url,
        'error': error
    }


def fib(n): return reduce(lambda x, _: x+[x[-1]+x[-2]],
                          range(n-2), [0, 1])


def file_data(data):
    with open('files/petition.txt', 'a') as f:
        f.write(f'{data}\n')


def create_file(data):
    with open('files/petition.txt', 'w') as f:
        for line in data:
            f.write(f'{line}\n')


def file_delete(id):
    match = f'_id:{id}'
    data_file = []
    f = codecs.open('files/petition.txt', 'r', 'utf-8')
    for linea in f:
        process = linea.rstrip()
        fragments = process.split('|')
        if(match == fragments[0]):
            app.logger.info(f'Delete registrie: {id}')
        else:
            data_file.append(process)
    f.close()
    app.logger.info(len(data_file))
    app.logger.info(data_file)
    create_file(data_file)
