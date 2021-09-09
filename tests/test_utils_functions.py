import unittest
import string

from utils import uuid_generator

class TestUtilsFunctions(unittest.TestCase):


    def test_generate_uuid(self):

        expected_uuid_size = 6
        generated_uuid = uuid_generator(
            size=expected_uuid_size
        )

        with self.subTest(generated_uuid=generated_uuid):
            self.assertIsInstance(generated_uuid, str)
        
        with self.subTest(generated_uuid=generated_uuid):
            self.assertEqual(
                len(generated_uuid),
                expected_uuid_size
            )

        with self.subTest(generated_uuid=generated_uuid):
            self.assertEqual(
                generated_uuid.lower(),
                generated_uuid
            )
