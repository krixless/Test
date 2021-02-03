import requests

token = {'Authorization': 'AgAAAAACIzn2AADLW9tUROwqf0CJqDKDAQzLquM'}
url = 'https://cloud-api.yandex.net/v1/disk/resources?path=Test'


def create_folder():
    r = requests.put(url, headers=token)
    return r


def delete_folder():
    r = requests.delete(url, headers=token)
    return r


def check_folder():
    r = requests.get(url, headers=token)
    return r
