import unittest

try:
    import sys
    import os

    sys.path.append(
        os.path.abspath(
            os.path.join(
                os.path.dirname(__file__), '../app'
            )
        )
    )
except:
    raise

from .test_create_shortened_url import *
from .test_utils_functions import *

if __name__ == '__main__':
    unittest.main(verbosity=2)