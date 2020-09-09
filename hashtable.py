import requests
from os.path import exists
from utilities.storagenode import servers


def hash_fn(key):
    return sum(bytearray(key, 'utf-8')) % 9


def upload(file_name):
    index = hash_fn(file_name)
    node = servers[index]

    file = {'avatar': open(file_name,  'rb')}
    print(f'Uploading: {file_name} To: {node.name} Host: {node.host}')

    return requests.post(f'http://{node.host}/upload-avatar', files=file).text


def fetch(file_name):
    index = hash_fn(file_name)
    node = servers[index]

    return requests.get(f'http://{node.host}/{file_name}').text


def create_and_upload():
    for i in range(10):
        if not exists(f'pic_{i}.txt'):
            f = open(f'pic_{i}.txt', 'x')
            f.write(f'contents of file {i}')
            f.close()
        upload(f'pic_{i}.txt')


def get_files():
    for i in range(10):
        print(fetch(f'pic_{i}.txt'))


# create_and_upload()
get_files()
