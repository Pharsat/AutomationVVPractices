import json
import unittest
from datetime import datetime

from api_testing.request_api.book import api_book as api


class ApirequestBooks(unittest.TestCase):
    now = datetime.now()

    def test_get_all_books(self, endpoint):
        self.response = api.get_all_books(endpoint)
        return self.response

    def test_post_new_book(self, endpoint, id, title, Description, PageCount, Excerpt, PublishDate):
        self.payload = json.dumps({
            "ID": int(id),
            "Title": "{}".format(title),
            "Description": "{}".format(Description),
            "PageCount": int(PageCount),
            "Excerpt": "{}".format(Excerpt),
            "PublishDate": "{}".format(PublishDate)
        })

        self.response = api.post_new_book(endpoint, self.payload)
        return self.response

    def test_delete_book(self, endpoint, id):
        self.response = api.delete_book(endpoint, id)

    def test_get_book_by_id(self, endpoint, id):
        self.response = api.get_book_by_id(endpoint, id)

    def test_put_book_by_id(self, endpoint, id, id_book, title, Description, PageCount, Excerpt, PublishDate):
        self.payload_put = json.dumps({
            "ID": int(id_book),
            "Title": "{}".format(title),
            "Description": "{}".format(Description),
            "PageCount": int(PageCount),
            "Excerpt": "{}".format(Excerpt),
            "PublishDate": "{}".format(PublishDate)
        })
        self.response_put = api.put_book_by_id(endpoint, id, self.payload_put)

    def validate_number_book(self, number_book):
        response_data = json.loads(self.response.text)
        len_book = len(response_data)
        self.assertEquals(len_book, number_book)

    def validate_code(self, code_expected):
        self.assertEquals(self.response.status_code, code_expected)

    def validate_new_book(self):
        self.assertEquals(json.loads(self.response.text), json.loads(self.payload))

    def validate_response_book(self):
        self.assertEquals(json.loads(self.response_put.text), json.loads(self.payload_put))

    def validate_book_by_id(self, id, title, Description, PageCount, Excerpt, PublishDate):
        self.response_text = json.loads((self.response.text).replace("\\r\\n", ""))
        self.payload2 = json.dumps({
            "ID": int(id),
            "Title": "{}".format(title.replace("\\r\\n", "")),
            "Description": "{}".format(Description.replace("\\r\\n", "")),
            "PageCount": int(PageCount),
            "Excerpt": "{}".format(Excerpt.replace("\\r\\n", "")),
            "PublishDate": self.response_text["PublishDate"]
        })
        self.assertEqual(self.response_text, json.loads(self.payload2))


if __name__ == '__main__':
    unittest.main()
