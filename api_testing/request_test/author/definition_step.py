import json
import unittest
from datetime import datetime
from api_testing.request_api.author import api_author as api


class ApiRequestAuthors(unittest.TestCase):
    now = datetime.now()

    def test_get_all_authors_by_book(self, endpoint, book_id):
        self.response = api.get_all_authors_by_book(endpoint, book_id)

    def test_get_all_authors(self, endpoint):
        self.response = api.get_all_authors(endpoint)

    def test_get_author(self, endpoint, author_id):
        self.response = api.get_author(endpoint, author_id)

    def test_create_author(self, endpoint, author_data):
        self.response = api.create_author(endpoint, author_data)

    def test_delete_author(self, endpoint, author_id):
        self.response = api.delete_author(endpoint, author_id)

    def test_update_author(self, endpoint, author_id, author_data):
        self.response = api.update_author(endpoint, author_id, author_data)

    def test_items_count(self, required_value):
        response_data = json.loads(self.response.text)
        self.assertEquals(required_value, len(response_data))

    def test_item_check(self):
        response_data = json.loads(self.response.text)
        self.item = response_data

    def test_validate_response_code(self, code):
        self.assertEquals(self.response.status_code, code)

    def text_validate_two_json_objects_are_equal(self, object_to_validate):
        self.assertEquals(json.loads(self.response.text), json.loads(object_to_validate))

    def test_validate_empty_response(self):
        print(self.response.text)
        self.assertEquals(self.response.text, "")




if __name__ == '__main__':
    unittest.main()
