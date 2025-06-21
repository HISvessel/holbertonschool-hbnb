"""init mrthod to call and run the whole app"""
from flask import Flask
from flask_restx import Api

def create_app():
    app = Flask(__name__)
    api = Api(app, version='1.0', title='Hbnb API', description='Hbnb Application API', doc='/api/v1')

    #Placeholder for API namespace(endpoints will be added later)
    #additional namespaces for places, reviews, and ammenities will be added later
    return app