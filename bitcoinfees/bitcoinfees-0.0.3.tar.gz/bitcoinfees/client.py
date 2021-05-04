import requests

API_URl = "https://bitcoinfees.earn.com/api/v1/"


def recommended():
    path = "fees/recommended"
    return request(path)


def request(path):
    url = API_URl + path

    response = requests.get(url)

    return response.json()
