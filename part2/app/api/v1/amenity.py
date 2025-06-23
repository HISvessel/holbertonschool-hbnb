"""creating this file for our first version of our amenity class entity:
pending changes, as this is for our initial file structure"""

from flask_restx import Namespace, fields, Resource
from app.services import facade

amenity_api = Namespace("amenity", description="Amenity endpoints")

amenity_model = amenity_api.model("AmenityModel", {
    "name": fields.String(required=True, description="Amenity name")
})
#amenity_get_model = amenity_api.model({}) # tempting
#amenity_update_model = amenity_api.model({})

@amenity_api.route("/")
class AmenityCreation(Resource):
    @amenity_api.expect(amenity_model, validate=True)
    @amenity_api.response(200, "Amenity added succesfully")
    @amenity_api.response(400, "Invalid amenity")
    def post(self):
        amenity_data = amenity_api.payload
        try:
            new_amenity = facade.create_amenity(amenity_data)
            return new_amenity.to_dict(), 200
        except ValueError as e:
            return {"error": str(e)}, 404

@amenity_api.route("/<string:amenity_id>")
class GetAmenity(Resource):
    @amenity_api.response(200, "Amenity retrieved!")
    @amenity_api.response(404, "Amenity not found.")
    def get(self, amenity_id):
        amenity = facade.get_amenity(amenity_id)
        if not amenity:
           return {"error": "Amenity not found"}, 404
        return amenity.to_dict(), 200

@amenity_api.route("/<string:amenity_id>")
class AmenityList(Resource):
    pass

@amenity_api.route("/<string:amenity_id>")
class UpdateAmenity(Resource):
    pass