from flask import Flask
from app.routes import register_routes
from app.logger import setup_logger

def create_app():
    logger = setup_logger()
    app = Flask(__name__)
    register_routes(app, logger)
    return app