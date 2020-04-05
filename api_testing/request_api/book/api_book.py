import requests

url = "https://fakerestapi.azurewebsites.net"


def get_all_books(endpoint):
    return requests.get(url + endpoint)


def post_new_book(endpoint, body):
    headers = {"Content-Type": "application/json"}
    return requests.post(url + endpoint, data=body, headers=headers)


def delete_book(endpoint, id):
    return requests.delete(url + endpoint + "/" + id)


def get_book_by_id(endpoint, id):
    return requests.get(url + endpoint + "/" + id)


def put_book_by_id(endpoint, id, body):
    headers = {"Content-Type": "application/json"}
    return requests.put(url + endpoint + "/" + id, data=body, headers=headers)
