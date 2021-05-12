from flask import Flask
from do_stuff import do_stuff


def create_app():
    flask_app = Flask(__name__)
    initialize_app(flask_app)
    return flask_app


def initialize_app(flask_app):
    flask_app.register_blueprint(do_stuff, url_prefix='/do_stuff')


app = create_app()


@app.route("/")
def hello():
    return "Hello World!"


if __name__ == "__main__":
    app.run()
