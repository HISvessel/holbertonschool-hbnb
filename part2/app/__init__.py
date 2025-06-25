"""init mrthod to call and run the whole app"""
from flask import Flask
from flask_restx import Api
from app.api.v1.user import user_api
from app.api.v1.amenity import amenity_api
from app.api.v1.places import places_api

def create_app():
    app = Flask(__name__)
    my_api = Api(app, version='1.0', title='Hbnb API', description='Hbnb Application API', doc='/api/v1')

    #Placeholder for API namespace(endpoints will be added later)
    #additional namespaces for places, reviews, and ammenities will be added later
    my_api.add_namespace(user_api, path="/v1/user")
    my_api.add_namespace(amenity_api, path="/v1/amenities")
    return app