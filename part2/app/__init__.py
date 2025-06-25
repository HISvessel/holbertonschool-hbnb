"""init mrthod to call and run the whole app"""
from flask import Flask
from flask_restx import Api
from app.api.v1.user import user_api
from app.api.v1.amenity import amenity_api
from app.api.v1.places import place_api
#from app.api.v1.review import review_api

def create_app():
    app = Flask(__name__)
    my_api = Api(app, version='1.0', title='Hbnb API', description='Hbnb Application API', doc='/api/v1')

    #Placeholder for API namespace(endpoints will be added later)
    #additional namespaces for places, reviews, and ammenities will be added later
    my_api.add_namespace(user_api, path="/v1/user")
    my_api.add_namespace(amenity_api, path="/v1/amenities")
    my_api.add_namespace(place_api, path="/v1/place")
    for rule in app.url_map.iter_rules():
        print(f"{rule.endpoint:30s} -> {rule.rule}")
    return app