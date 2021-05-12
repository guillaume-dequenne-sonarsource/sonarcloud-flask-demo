from flask import Blueprint, Response

do_stuff = Blueprint('cookies', __name__)


@do_stuff.route('/')
def index():
    return 'Cookie configuration'


# http://localhost:5000/do_stuff/unsafe
@do_stuff.route('/unsafe')
def unsafe():
    response = Response('Hey there!')
    return response
