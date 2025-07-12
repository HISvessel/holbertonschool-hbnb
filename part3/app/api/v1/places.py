"""the first creation of our place class; pending changes, as these are for structure"""
from flask_restx import Namespace, fields, Resource, marshal_with
from flask_jwt_extended import get_jwt_identity, jwt_required
from app.services import facade



place_api = Namespace("place", description="Place endpoints")

place_model = place_api.model("PlaceModel", {
    "title": fields.String(required=True, description="place name"),
    "description": fields.String(required= True, description="description of place"),
    "price": fields.Float(required=True, description="price for booking place"),
    #"coordinates": fields.Nested(place_api.model("Coordinates", {
    #    "latitude": fields.Float,
    #    "longitude": fields.Float
    #})),
    "latitude": fields.Float,
    "longitude": fields.Float,
    "owner_id": fields.String(required=True, description="owner of the place"),
    #"owner": fields.String(required=True, description='owner of the place'),
    "amenities": fields.List(fields.String, description="List of amenity IDs"),
    "reviews": fields.List(fields.String, description="List of review IDs")
})

place_output_model = place_api.model("PlaceOutput", {
    "id": fields.String,
    "title": fields.String,
    "description": fields.String,
    "created_at": fields.DateTime,
    "updated_at": fields.DateTime,
    "price": fields.Float,
  #potentially to set as coordinates for more accurate representation
    #"coordinates": fields.Nested(place_api.model("Coordinates", {
    #    "latitude": fields.Float,
    #    "longitude": fields.Float
    #})),
    "latitude": fields.Float,
    "longitude": fields.Float,
    "owner_id": fields.String,
    "amenities": fields.List(fields.String, description="List of amenity IDs"),
    "reviews": fields.List(fields.String, description="List of review IDs")
})

place_update_model = place_api.model("PlaceUpdateModel", {
    "title": fields.String(required=True, description="place name"),
    "description": fields.String(required= True, description="description of place"),
    "price": fields.Float(required=True, description="price for booking place"),
    "owner_id": fields.String(required=True, description="owner of the place"),
    "amenitites": fields.List(fields.String)
})

@place_api.route("/")
class CreatePlace(Resource):
    @place_api.expect(place_model, validate=True)
    @place_api.response(200, "Successful creation of place")
    @place_api.response(400, "Cannot add place, already exists") # pending deletion
    @place_api.response(400, "Invalid price set") # pending deletion
    @place_api.response(400, "Invalid user ID")
    @marshal_with(place_output_model)
    @jwt_required()
    def post(self):
      current_user = get_jwt_identity()
      place_data = place_api.payload
      place_data["owner_id"] = current_user
      try:
          place = facade.create_place(place_data)
          return place, 201
      except Exception as e:
          return place_api.abort(404, str(e))

@place_api.route("/all")
class PlaceList(Resource):
    @place_api.response(201, "Places retrieved.")
    @place_api.response(400, "Places could not be found.")
    def get(self):
        place_list = facade.get_all_places()
       # place_data = [place.to_dict() for place in place_list]
        return place_list, 200
    
@place_api.route("/<string:place_id>")
class GetPlace(Resource):
    @place_api.response(201, "Place retrieved.")
    @place_api.response(404, "Place not found.")
    @marshal_with(place_output_model)
    def get(self, place_id):
        place = facade.get_place(place_id)
        if not place:
            place_api.abort(404, "Place not found.")
        return place, 200

class UpdatePlace(Resource):
    @place_api.expect(place_update_model, validate=True)
    @place_api.response(200, "Place updated")
    @place_api.response(404, "Invalid place")
    @place_api.response(400, "Invalid data")
    @marshal_with(place_output_model)
    @jwt_required()
    def put(self, place_id):
        data = place_api.payload
        place = facade.get_place(place_id)
        current_user = get_jwt_identity() #retrieving current user upon method
        
        #checking that place id maches the current user's id
        if place.owner_id != current_user["id"]:
            place_api.abort(403, "Unauthorized action.")
        if not place:
            place_api.abort(404, "Place not found")
        allowed_fields = ["title", "description", "price", "owner_id", "amenities"]
        updated_data = {}
        for key in data:
            if key not in allowed_fields:
                continue
            updated_data[key] = data[key]
        updated_place = facade.update_place(place_id, updated_data)
        return updated_place, 200
