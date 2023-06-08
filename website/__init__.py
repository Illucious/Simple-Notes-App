from flask import Flask
from .views import views
from .auth import auth


def create_app():
    app = Flask(__name__)
    app.config[
        "SECRET_KEY"
    ] = "THIS IS THE SECret key"  # a secret key that has to be made for each project

    app.register_blueprint(views, urlprefix="/")
    app.register_blueprint(auth, urlprefix="/")

    return app
