"""the first creation of our place class; pending changes, as these are for structure"""
from flask_restx import Namespace, fields, Resource, marshal_with
from app.services import facade



place_api = Namespace("place", description="Place endpoints")

place_model = place_api.model("PlaceModel", {
    "title": fields.String(required=True, description="place name"),
    "description": fields.String(required= True, description="description of place"),
    "price": fields.Float(required=True, description="price for booking place"),
  #potentially to set as coordinates for more accurate representation
    "latitude": fields.Float(required=True, description="geoposition of place"),
    "longitude": fields.Float(required=True, description="geolocation of place"),
    "owner": fields.String(required=True, description="owner of the place"),
    "amenitites": fields.Integer,
    "reviews": fields.Integer
})

place_output_model = place_api.model("PlaceOutput", {
    "id": fields.String,
     "title": fields.String,
    "description": fields.String,
    "created_at": fields.String,
    "updated_at": fields.String,
    "price": fields.Float,
  #potentially to set as coordinates for more accurate representation
    "latitude": fields.Float,
    "longitude": fields.Float,
    "owner": fields.String,
    "amenitites": fields.Integer, #to set as a sub entity of an existing entity
    "reviews": fields.Integer #to set as a sub entity of an existing entity
})

place_update_model = place_api.model("PlaceUpdateModel", {
     "title": fields.String(required=True, description="place name"),
    "description": fields.String(required= True, description="description of place"),
    "price": fields.Float(required=True, description="price for booking place"),
    "owner": fields.String(required=True, description="owner of the place"),
    "amenitites": fields.Integer,
    "reviews": fields.Integer
})