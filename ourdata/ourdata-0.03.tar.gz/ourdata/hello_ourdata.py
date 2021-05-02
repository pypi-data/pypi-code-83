import requests

def hello_data():
    print("Hello Data!")

def test_request():
    print(requests.get("https://rickandmortyapi.com/api/character/?page=2"))