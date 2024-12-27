# Initialization file for flask app

from flask import Flask

def create_app():
    # create a flask instance 
    init_app = Flask("Initialization",__name__)
    
    # importing blueprints to register with app 
    from .routes import app as app_routes
    init_app.register_blueprint(app_routes)

    return init_app