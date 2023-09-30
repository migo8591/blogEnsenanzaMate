from flask import Flask
from .public import public_bp



def create_app(config):
    app = Flask(__name__)

    app.register_blueprint(public_bp)
    app.config.from_object(config)
    return app