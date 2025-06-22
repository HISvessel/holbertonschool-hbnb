from flask_restx import Resource, Namespace, fields
from app.services import facade


api = Namespace("users", description="User operations")

user_model = api.model('User', {
    "first_name": fields.String(required=True, description="First name of the user"),
    "last_name": fields.String(required=True, description="Last name of the user"),
    "email": fields.String(required=True, description="User's email"),
    "password": fields.String(required=True, description=("User's password"))
})

@api.route("/")
class UserList(Resource):
    @api.expect(user_model, validate=True)
    @api.response(201, "User creation success")
    @api.response(400, "Email already registered to existing user")
    @api.response(400, "Invalid email entered")
    @api.response(400, 'Invalid password')
    def post(self):
        user_data = api.payload

        existing_user = facade.get_user_by_email(user_data['user_email'])
        if existing_user:
            return {"error": "Email already registered"}, 400
        new_user = facade.create_user(user_data)
        return new_user.to_dict, 201
