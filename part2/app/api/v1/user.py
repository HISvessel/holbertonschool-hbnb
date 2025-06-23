from flask_restx import Resource, Namespace, fields
from app.services import facade


user_api = Namespace("users", description="User operations")

user_model = user_api.model('User', {
    "first_name": fields.String(required=True, description="First name of the user"),
    "last_name": fields.String(required=True, description="Last name of the user"),
    "email": fields.String(required=True, description="User's email"),
    "password": fields.String(required=True, description=("User's password")),
    "is_admin": fields.Boolean(required=False, default=False)
})

user_login_model = user_api.model('UserLogin', {
    "email": fields.String(required=True),
    "password": fields.String(required=True)
})

@user_api.route("/")
class UserList(Resource):
    @user_api.expect(user_model, validate=True)
    @user_api.response(201, "User creation success")
    @user_api.response(400, "Email already registered to existing user")
    @user_api.response(400, "Invalid email entered")
    @user_api.response(400, 'Invalid password')
    def post(self):
        user_data = user_api.payload

        try:
            new_user = facade.create_user(user_data)
            return new_user.to_dict(), 201
        except ValueError as e:
            return {"error": str(e)}, 400

@user_api.route("/login")
class UserLogin(Resource):
    @user_api.expect(user_login_model, validate=True)
    @user_api.response(200, "Login successful")
    @user_api.response(401, "Invalid user or email")
    def post(self):
        data = user_api.payload
        email = data.get("email")
        #password = data.get("password") #Temporary block, attaining password through different method
        user = facade.get_user_by_email(email)

        if not user:
            return{"error": "User not found"}, 404
        if not user.verify_password(data["password"]):
            return {"error": "Invalid password"}, 401
        return user.to_dict(), 200
