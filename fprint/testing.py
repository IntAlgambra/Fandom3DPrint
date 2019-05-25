import unittest
import requests

URL = 'http://5.253.60.32'

class TestWebsite(unittest.TestCase):

    def test_is_available(self):
        r = requests.get(URL)
        status_code = r.status_code
        self.assertEqual(status_code, 200)

if __name__ == '__main__':
    unittest.main()
