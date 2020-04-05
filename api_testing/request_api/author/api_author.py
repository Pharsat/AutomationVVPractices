import requests

url = "https://fakerestapi.azurewebsites.net"


def get_all_authors_by_book(endpoint, book_id):
    complete_url = (url + endpoint).format(book_id)
    print(complete_url)
    return requests.get(complete_url)


def get_all_authors(endpoint):
    complete_url = url + endpoint
    print(complete_url)
    return requests.get(complete_url)


def get_author(endpoint, author_id):
    complete_url = (url + endpoint).format(author_id)
    print(complete_url)
    return requests.get(complete_url)


def create_author(endpoint, author_data):
    headers = {"Content-Type": "application/json"}
    return requests.post(url + endpoint, data=author_data, headers=headers)


def delete_author(endpoint, author_id):
    complete_url = (url + endpoint).format(author_id)
    print(complete_url)
    return requests.delete(complete_url)


def update_author(endpoint, author_id, author_data):
    headers = {"Content-Type": "application/json"}
    return requests.put((url + endpoint).format(author_id), data=author_data, headers=headers)