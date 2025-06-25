"""the first creation of our place class; pending changes, as these are for structure"""
from flask_restx import Namespace, fields, Resource, marshal_with
from app.services import facade



place_api = Namespace("place", description="Place endpoints")

place_model = place_api.model("PlaceModel", {
    "title": fields.String(required=True, description="place name"),
    "description": fields.String(required= True, description="description of place"),
    "price": fields.Float(required=True, description="price for booking place"),
    "coordinates": fields.Nested(place_api.model("Coordinates", {
        "latitude": fields.Float,
        "longitude": fields.Float
    })),
    "owner": fields.String(required=True, description="owner of the place"),
    "amenities": fields.List(fields.String, description="List of amenity IDs"),
    "reviews": fields.List(fields.String, description="List of review IDs")
})

place_output_model = place_api.model("PlaceOutput", {
    "id": fields.String,
    "title": fields.String,
    "description": fields.String,
    "created_at": fields.String,
    "updated_at": fields.String,
    "price": fields.Float,
  #potentially to set as coordinates for more accurate representation
    "coordinates": fields.Nested(place_api.model("Coordinates", {
        "latitude": fields.Float,
        "longitude": fields.Float
    })),
    "owner": fields.String,
    "amenities": fields.List(fields.String, description="List of amenity IDs"),
    "reviews": fields.List(fields.String, description="List of review IDs")
})

place_update_model = place_api.model("PlaceUpdateModel", {
    "title": fields.String(required=True, description="place name"),
    "description": fields.String(required= True, description="description of place"),
    "price": fields.Float(required=True, description="price for booking place"),
    "owner": fields.String(required=True, description="owner of the place"),
    "amenitites": fields.List(fields.String)
})

place_api.route("/")
class CreatePlace(Resource):
    place_api.expect(place_model, validate=True)
    place_api.response(200, "Successful creation of place")
    place_api.response(400, "Cannot add place, already exists") # pending deletion
    place_api.response(400, "Invalid price set") # pending deletion
    place_api.response(400, "Invalid user ID")
    @marshal_with(place_output_model)
    def post(self):
      place_data = place_api.payload
      try:
          place = facade.create_place(place_data)
          return place, 201
      except Exception as e:
         return place_api.abort(404, str(e))
