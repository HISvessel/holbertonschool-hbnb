"""creating this file for our first version of our amenity class entity:
pending changes, as this is for our initial file structure"""

from flask_restx import Namespace, fields, Resource
from app.services import facade

amenity_api = Namespace("amenity", description="Amenity endpoints")

amenity_model = amenity_api.model("AmenityModel", {
    "name": fields.String(required=True, description="Amenity name")
})

amenity_update_model = amenity_api.model("AmenityUpdate", {
    "name": fields.String(required=True, description="Updated amenity data")
})

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

    @amenity_api.response(200, "Amenities obtained")
    @amenity_api.response(400, "Cannot locate amenities")
    def get(self):
        amenity_list = facade.get_all_amenities()
        amenity_data = [amenity.to_dict() for amenity in amenity_list]
        return amenity_data, 200

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
class UpdateAmenity(Resource):
    @amenity_api.expect(amenity_update_model, validate=True)
    @amenity_api.response(200, "Amenity successfully updated")
    @amenity_api.response(404, "Amenity cannot be found")
    def put(self, amenity_id):
        amenity = facade.get_amenity(amenity_id)
        if not amenity:
            return {"error": "Amenity not found"}, 404
        data = amenity_api.payload
        allowed_field = ["name"]
        updated_data = {}
        for key in data:
            if key not in allowed_field:
                continue
            updated_data[key] = data[key]
        updated_amenity = facade.update_amenity(amenity_id, updated_data)
        return updated_amenity.to_dict(), 200
