import flask
import unittest
import json

from app import db, app

class TestGetShortedLink(unittest.TestCase):


    def setUp(self):
        app.config.update(
            SQLALCHEMY_DATABASE_URI='sqlite:///database/test_database.sqlite',
            TESTING=True
        )
        self.test_client = app.test_client()
        db.create_all()

    def tearDown(self):
        return
        db.session.remove()
        db.drop_all()

    def test_get_with_invalid_uuid(self):

        response = self.test_client.get('/AAAAAA')
        expected_response_data = {
            'status': 'error',
            'message': 'The requested URL was not found'
        }

        response_data = json.loads(
            response.get_data(as_text=True)
        )

        self.assertEqual(response_data, expected_response_data)
        self.assertEqual(response.status_code, 404)
    

    def test_get_with_valid_uuid(self):

        original_url_to_short = 'https://github.com/LuisHenriqueDaSilv'
        short_url_response = self.test_client.post(
            '/short',
            data=dict(
                url=original_url_to_short
            )
        )
        short_url_response_data = json.loads(
            short_url_response.get_data(as_text=True)
        )

        get_url_response = self.test_client.get(
            '/' + short_url_response_data["shorted_url_uuid"] 
        )

        self.assertTrue(
            original_url_to_short in str(get_url_response.data)
        )
