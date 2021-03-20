import logging
from logging.handlers import RotatingFileHandler, TimedRotatingFileHandler
import traceback
import time
import csv

def ternary():
    condition = False
    x = 1 if condition else 0
    print('ternary', x)


def big_numbers():
    a = 100_000_000_000
    b = 100_000_000
    total = a + b
    print(f'total: {total:,}')


def context_manager():
    with open('addresses.csv', 'r') as f:
        content = f.read()
    print(content)


def enum():
    fruits = ['abacaxi', 'morango', 'kiwi', 'maçã', 'banana', 'manga']
    planets = ['mars', 'jupiter', 'saturn', 'earth', 'venus', 'mercury']
    colors = ['red', 'green', 'blue', 'yellow', 'white', 'black', 'purple']

    for index, fruit in enumerate(fruits, start=1):
        print(index, fruit)
    print('-----')
    for fruit, planet, color in zip(fruits, planets, colors):
        print(fruit, ' - ', planet, ' - ', color)
    print('-----')
    for value in zip(fruits, planets, colors):
        print(value)
    print('-----')


def unpack():
    a, _ = (1, 2)
    print(a)
    print('-----')
    a, b, *_ = (1,2,3,4,5,6,7,8,9)
    print(a)
    print(b)
    print('---')
    a, b, *_, d = (1,2,3,4,5,6,7,8,9)
    print(a)
    print(b)
    print(d)
    print('---')


class Person():
    pass


def attr():
    person = Person()
    k = 'first'
    v = 'João'
    setattr(person, k, v)
    print(person.first)
    f = getattr(person, k)
    print(f)
    print('-----')
    person_info = {'first':'Maria', 'last':'Silva'}
    for key, value in person_info.items():
        setattr(person, key, value)
    print(person.first)
    print(person.last)
    print('-----')


def traceb():
    try:
        raise NotImplementedError('Not implemented')
    except Exception as e: 
        t = traceback.format_exc()
        print(t)

def listset():
    with open('hw_25000.csv', 'r') as f:
        lines = f.readlines()
        #lines = f.readlines()[1:20_000]
        #for line in lines:
        #    print(line, ' --- ', line.split(",")[1])
        lines_set = set(lines)


        ret = []
        s = time.time()
        for i in range(1000):
            ret.append(str(i) in  lines)
        print('time taken: ', time.time() - s)

        s = time.time()
        ret = []
        for i in range(1000):
            ret.append(str(i) in  lines_set)
        print('time taken set: ', time.time() - s)
        print('-----')


def add_to_agg_list(arr, aggregate_list=None):
    if isinstance(aggregate_list, type(None)):
        aggregate_list = []
    for a in arr:
        aggregate_list.append(a)
    return aggregate_list


def argumentos(codigo, nome='anonimo'):
    print('codigo:', codigo, 'nome:', nome)
    print('-----')


def variable_arguments(*b):
    c = 0

    for i in b:
        c += i

    print(c)
    print('-----')

def variable_kv_arguments(name, **kwargs):
    print(name)
    for k,v in kwargs.items():
        print('key:', k, 'value: '+ str(v))

def main():
    fruits = ['abacaxi', 'morango', 'kiwi', 'maçã', 'banana', 'manga']
    ternary()
    big_numbers()
    context_manager()
    enum()
    unpack()
    attr()
    traceb()
    listset()
    print(add_to_agg_list(fruits))

    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    
    formatter = logging.Formatter('%(asctime)s:%(name)s:%(levelname)s:%(message)s')

    file_handler = RotatingFileHandler('logs/tips.log', mode='a',maxBytes=1_000, backupCount=2, encoding=None, delay=False)
    
    time_handler = TimedRotatingFileHandler('logs/time.log', when='M', interval=1, backupCount=2, encoding=None, delay=False, utc=False, atTime=None)

    #file_handler = TimedRotatingFileHandler('logs/tips.log',
    #                               when="midnight",
    #                               interval=1)

    #file_handler = logging.FileHandler('logs/tips.log')

    #file_handler.setLevel(logging.DEBUG)

    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    logger.addHandler(time_handler)

    #stream_handler = logging.StreamHandler()
    #stream_handler.setFormatter(formatter)
    #logger.addHandler(stream_handler)

    logger.debug('custom debugging...')
    #logging.basicConfig(filename='logs/logs.log', level=logging.DEBUG,
    #                    format='%(asctime)s:%(levelname)s:%(message)s')
    #logging.debug('debugging...')
    try:
        r = 2/0
        print(str(r))
    except ZeroDivisionError:
        logger.exception('divisão por zero')
    else:
        print('OK')

    argumentos(1, 'Maria Silva')
    argumentos(2)

    variable_arguments(10, 20, 30, 40)

    variable_kv_arguments('Scott', age=30, city='Miami', mob=9876543210)

if __name__ == '__main__':
    main()