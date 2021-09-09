from functools import wraps
from app import app

def handle_error(function):

    @wraps(function)
    def wrapper( *args, **kwargs):
        try:
            return function(*args, **kwargs)
        except Exception as error:
            
            app.logger.error(error)
            return {
                'status': 'error',
                'message': 'Something unexpected happened'
            }, 500

    return wrapper