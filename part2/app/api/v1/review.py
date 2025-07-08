"""creating the file for our review class entity:
pending changes, as this is for our initial folder structure"""
from flask_restx import Namespace, fields, Resource, marshal_with
from app.services import facade

review_api = Namespace("review", description="Review endpoints")

review_model = review_api.model("ReviewModel", {
    "id": fields.String(description='Review ID'),
    "title": fields.String(required=True, description="Title for a review"),
    "comment": fields.String(required=True, description="Comments in a review"),
    "rating": fields.Integer,
    "user_id": fields.String(required=True, description="Reviewers ID"),
    "place_id": fields.String(required=True, description="Place's ID")
})

review_output_model = review_api.model("ReviewOutputModel", {
    "title": fields.String,
    "comment": fields.String,
    "rating": fields.Integer,
    "created_at": fields.String,
    "updated_at": fields.String,
    })

review_update_model = review_api.model("ReviewUpdate", {
    "title": fields.String(required=True, description="Updated amenity data"),
    "comment": fields.String(required=True, description="new comment for the place"),
    "rating": fields.Integer
})

@review_api.route("/")
class ReviewCreation(Resource):
    @review_api.expect(review_model, validate=True)
    @review_api.response(200, "Review added succesfully")
    @review_api.response(400, "Invalid review")
    @marshal_with(review_output_model)
    def post(self):
        review_data = review_api.payload
        try:
            new_review = facade.create_review(review_data)
            return new_review, 201
        except ValueError as e:
            return {"error": str(e)}, 404

    @review_api.response(200, "Reviews obtained")
    @review_api.response(400, "Cannot locate reviews")
    def get(self):
        review_list = facade.get_all_amenities()
        review_data = [review.to_dict() for review in review_list]
        return review_data, 200

@review_api.route("/<string:review_id>")
class GetReview(Resource):
    @marshal_with(review_output_model)
    @review_api.response(200, "Review retrieved!")
    @review_api.response(404, "Review not found.")
    def get(self, review_id):
        review = facade.get_review(review_id)
        if not review:
           review_api.abort(404, "Review not found")
        return review, 201


@review_api.route("/<string:review_id>")
class UpdateReview(Resource):
    @review_api.expect(review_update_model, validate=True)
    @review_api.response(200, "Amenity successfully updated")
    @review_api.response(404, "Amenity cannot be found")
    @marshal_with(review_output_model)

    def put(self, review_id):
        review = facade.get_review(review_id)
        if not review:
            review_api.abort(404, "Cannot find review.")
        data = review_api.payload
        allowed_field = ["title", "comment", "rating"]
        updated_data = {}
        for key in data:
            if key not in allowed_field:
                continue
            updated_data[key] = data[key]
        updated_review = facade.update_review(review_id, updated_data)
        return updated_review, 200
    
    @review_api.route("/string:review_id>")
    class DeleteReview(Resource):
        pass
