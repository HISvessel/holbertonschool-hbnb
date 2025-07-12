"""creating the file for our review class entity:
pending changes, as this is for our initial folder structure"""
from flask_restx import Namespace, fields, Resource, marshal_with
from flask_jwt_extended import get_jwt_identity, jwt_required
from app.services import facade

review_api = Namespace("review", description="Review endpoints")

review_model = review_api.model("ReviewModel", {
    "title": fields.String(required=True, description="Title for a review"),
    "comment": fields.String(required=True, description="Comments in a review"),
    "rating": fields.Integer,
    "place_id": fields.String(required=True, description="Place's ID")
})

review_output_model = review_api.model("ReviewOutputModel", {
    "id": fields.String, #will test to confirm this field is the user_id or review_id
    "title": fields.String,
    "comment": fields.String,
    "rating": fields.Integer,
    "user": fields.String,# pending deletion. must test if
    "place": fields.String,
    "created_at": fields.String,
    "updated_at": fields.String,
    })

review_update_model = review_api.model("ReviewUpdate", {
    "title": fields.String(required=True, description="Updated amenity data"),
    "comment": fields.String(required=True, description="new comment for the place"),
    "rating": fields.Integer,
})

@review_api.route("/")
class ReviewCreation(Resource):
    @review_api.expect(review_model, validate=True)
    @review_api.response(200, "Review added succesfully")
    @review_api.response(400, "Invalid review")
    @marshal_with(review_output_model)
    @jwt_required() #token verification required
    def post(self):
        review_data = review_api.payload
        current_user = get_jwt_identity() #user authentication
        review_data["user_id"] = current_user #binds created review to session user's id

        #find the place's owner id
        place_id = review_data["place_id"]
        place = facade.get_place(place_id)

        all_reviews = facade.get_all_reviews()
        try:
            if not place:
                review_api.abort(401, "Cannot add review. Place does not exist.")
            #testing model to block a place owner reviewing their own place
            if place.owner_id == current_user:
                review_api.abort(403, "You cannot review your own place")
            
            #testing model to block a user from reviewing the same place twice
            for review in all_reviews:
                if review.user_id == current_user and review.place_id == review_data["place_id"]:
                    review_api.abort(403, "You have already reviewed this place")

            new_review = facade.create_review(review_data)
            return new_review, 201
        except ValueError as e:
            return {"error": str(e)}, 404

    @review_api.response(200, "Reviews obtained")
    @review_api.response(400, "Cannot locate reviews")
    def get(self):
        review_list = facade.get_all_reviews()
        review_data = [review.to_dict() for review in review_list]
        return review_data, 200

@review_api.route("/<string:review_id>")
class ReviewDetails(Resource):
    @marshal_with(review_output_model)
    @review_api.response(200, "Review retrieved!")
    @review_api.response(404, "Review not found.")
    def get(self, review_id):
        review = facade.get_review(review_id)
        if not review:
           review_api.abort(404, "Review not found")
        return review, 200


    @review_api.expect(review_update_model, validate=True)
    @review_api.response(200, "Amenity successfully updated")
    @review_api.response(404, "Amenity cannot be found")
    @marshal_with(review_output_model)
    @jwt_required()
    def put(self, review_id):
        current_user = get_jwt_identity() #authenticates session token
        review = facade.get_review(review_id) #obtains review by id. string
        if not review: #checks for the existence of a review
            review_api.abort(404, "Cannot find review.")
        
        #searches for app user's id and matches it to the session user's id
        if review.user_id != current_user:
            review_api.abort(403, "Unauthorized action")
        data = review_api.payload
        allowed_field = ["title", "comment", "rating"]
        updated_data = {}
        for key in data:
            if key not in allowed_field:
                continue
            updated_data[key] = data[key]
        updated_review = facade.update_review(review_id, updated_data)
        return updated_review, 200

    @review_api.response(200, "Review successfully deleted")
    @jwt_required()
    def delete(self, review_id):
        current_user = get_jwt_identity()
        review = facade.get_review(review_id)
        if not review:
            return {"error": "Review does not exist"}, 404
        
        #matches review's user id to the session user's token
        if review.user_id != current_user:
            return {"error": "Unauthorized action."}, 403
        facade.delete_review(review_id)
        return {"message": "Review deleted successfully"}, 200
