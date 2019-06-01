import unittest
import urllib
from flask import Flask
from flask_testing import TestCase
from main import app
from flask import json


class MyTest(TestCase):

    def create_app(self):
        """
        create the app with a predictor
        :return: app
        """
        return app

    def setUp(self):
        """
        set up the application for client access
        :return:
        """

        self.app = self.app.test_client()

    def test_flask_application_is_up_and_running(self):
        """
        validate index is working
        :return:
        """
        response = self.client.get('/')
        self.assertTemplateUsed('index.html')
        self.assert200(response)

    def test_json(self):
        """
        test for predict if working with json access
        :return:
        """
        response = app.test_client().get(
            "/get_info?plate=abc-123&date=2019%2F05%2F30+21%3A10%3A10"
        )
        self.assert200(response)
        self.assertEqual(response.json, dict(
            info='Plate :abc-123 </br> Provincial: Unknown </br> Type: private vehicle </br> Can road: Yes </br>'
        ))


if __name__ == '__main__':
    unittest.main()