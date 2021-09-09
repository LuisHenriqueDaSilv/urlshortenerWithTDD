from flask import Blueprint, render_template

#Middlewares
from .middlewares.handle_error import handle_error

#Controllers
from .controller import Controller


router = Blueprint(
    'routes',
    __name__
)

@router.route('/short', methods=['POST'])
@handle_error
def create(*args, **kwargs):
    return Controller.create(*args, **kwargs)

@router.route('/', methods=['GET'])
@handle_error
def get_short_page():
    return render_template('short_url.html')

@router.route('/<uuid>', methods=['get'])
@handle_error
def read(*args, **kwargs):
    return Controller.read(*args, **kwargs)

