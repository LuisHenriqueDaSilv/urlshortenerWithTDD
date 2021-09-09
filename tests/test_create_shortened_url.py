import unittest
import json
import requests

from app import app, db

class TestCreateShortenedUrl(unittest.TestCase):

    
    def setUp(self):
        app.config.update(
            SQLALCHEMY_DATABASE_URI='sqlite:///database/test_database.sqlite',
            TESTING=True
        )
        self.test_client = app.test_client()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_create_with_all_params_valid(self):

        response = self.test_client.post(
            '/short',
            data=dict(
                url="https://google.com/"
            )
        )
        response_data = json.loads(
            response.get_data(as_text=True)
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response_data['status'], 'ok')
        self.assertIsNotNone(response_data['shorted_url_uuid'])
    
    def test_create_without_url_to_short(self):

        response = self.test_client.post(
            '/short'
        )
        expected_response_data = {
            'status': 'error',
            'message': 'Url to short not provided'
        }
        response_data = json.loads(
            response.get_data(as_text=True)
        )

        self.assertEqual(response_data, expected_response_data)
        self.assertEqual(response.status_code, 400)
    
    def test_create_with_invalid_url(self):

        response = self.test_client.post(
            '/short',
            data=dict(
                url="something text"
            )
        )
        response_data = json.loads(
            response.get_data(as_text=True)
        )
        expected_response_data = {
            'status': 'error',
            'message': 'Invalid url'
        }

        self.assertEqual(response_data, expected_response_data)
        self.assertEqual(response.status_code, 400)
