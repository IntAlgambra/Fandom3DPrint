import unittest
import requests
from ..models import Question, ModelingOrder, PrintingOrder
import os

HOST = 'http://d01bcd64.ngrok.io/'

PROXY_LIST = [
    '193.68.17.46:58558',
    '93.77.115.167:58097',
    '35.247.152.119:3128',
    '212.13.103.54:53263',
    '95.58.161.180:30937',
]

class TestMain(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('lets set up some tests')
        Question.objects.using('testing').all().delete()
        ModelingOrder.objects.using('testing').all().delete()
        PrintingOrder.objects.using('testing').all().delete()

    def setUp(self):
        self.session = requests.session()
        self.get_responce = self.session.get(HOST)
        self.csrftoken = self.session.cookies['csrftoken']

    def test_main(self):
        self.assertEqual(self.get_responce.status_code, 200)

    def test_feedback(self):
        payload = {
            'csrfmiddlewaretoken': self.csrftoken,
            'name': 'John Smith',
            'email': 'johnsmith@matrix.com',
            'message_text': 'Lorem Ipsum',
            'captcha_handler': '123456'
        }
        post_responce = self.session.post(HOST+'ask_question/', data=payload)
        q = Question.objects.using('testing').filter(sender_name = payload['name']).first()
        self.assertEqual(post_responce.status_code, 200)
        self.assertEqual(q.sender_name, 'John Smith')

    def test_printing_form(self):
        files = {'3d_file': open('main/tests/test_file.STL', 'rb')}
        payload = {
            'csrfmiddlewaretoken': self.csrftoken,
            'name': 'John Smith',
            'email': 'johnsmith@matrix.com',
            'material': 'PLA',
            'color': 'red',
            'quality': 'HIGH',
            'captcha_handler': '123456'
        }
        post_responce = self.session.post(HOST+'order_printing/', files=files, data=payload)
        order = PrintingOrder.objects.using('testing').filter(sender_name=payload['name']).first()
        self.assertEqual(order.sender_name, 'John Smith')
        self.assertEqual(post_responce.status_code, 200)

    def test_modeling_form(self):
        files = {'3d_file': open('main/tests/test_file.STL', 'rb')}
        payload = {
            'csrfmiddlewaretoken': self.csrftoken,
            'name': 'John Smith',
            'email': 'johnsmith@matrix.com',
            'model_description': 'Lorem Ipsum',
            'captcha_handler': '123456'
        }
        post_responce = self.session.post(HOST+'order_modeling/', files=files, data=payload)
        order = ModelingOrder.objects.using('testing').filter(sender_name=payload['name']).first()
        self.assertEqual(order.sender_name, 'John Smith')
        self.assertEqual(post_responce.status_code, 200)

if __name__ == '__main__':
    unittest.main()

