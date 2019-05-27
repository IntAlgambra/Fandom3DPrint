import unittest
import requests
from main.models import Question, PrintingOrder, ModelingOrder
import sqlite3

HOST = 'http://9ce92ed1.ngrok.io'

class TestMain(unittest.TestCase):

    def test_main(self):
        pass

    def test_feedback(self):
        session = requests.session()
        session.get(HOST)
        csrftoken = session.cookies['csrftoken']
        payload = {
            'csrfmiddlewaretoken': csrftoken,
            'name': 'John Smith',
            'email': 'johnsmith@matrix.com',
            'message_text': 'Lorem Ipsum',
            'captcha_handler': '123456'
        }
        responce = session.post(HOST+'ask_question/', data=payload)
        q = Question.objects.filter(sender_name = payload['name'])
        print(q)
        self.assertEqual(responce.status_code, 200)

    def test_printing_form(self):
        pass

    def test_modeling_form(self):
        pass
        

if __name__ == '__main__':
    unittest.main()