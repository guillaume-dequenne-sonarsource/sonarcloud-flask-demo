from flask import Blueprint, Response, request
from flask import redirect as flask_redirect

do_stuff = Blueprint('cookies', __name__)


@do_stuff.route('/')
def index():
    return 'Cookie configuration'


# http://localhost:5000/do_stuff/unsafe
@do_stuff.route('/unsafe')
def unsafe():
    response = Response('Hey there!')
    return response


# http://localhost:5000/do_stuff/redirect1?url=https://www.sonarsource.com
@do_stuff.route('/redirect1')
def redirect1():
    url = request.args["url"]
    return flask_redirect(url)
