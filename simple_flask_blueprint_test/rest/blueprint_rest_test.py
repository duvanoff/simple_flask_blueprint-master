import unittest
from flask import Flask
from simple_flask_blueprint.rest.blueprint_rest import bp


class SimpleBlueprintRestTest(unittest.TestCase):

    def setUp(self):
        self.app = Flask(__name__)
        self.app.register_blueprint(bp, url_prefix='/test')
        self.tester = self.app.test_client(self)

    def test_say_hallo(self):
        response = self.tester.get('/test/', content_type='application/json')
        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.data, 'Hallo!')
        response = self.tester.get('/test/Kalimaha/', content_type='application/json')
        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.data, 'Hallo Kalimaha!')
