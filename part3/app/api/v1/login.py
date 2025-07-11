"""this module creates paths for user login authentication adn authorization"""
from flask_restx import Namespace, Resource, fields, marshal, marshal_with
from app.services import facade
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity


"""this is our user API route model"""
login_api = Namespace("login", description="authentication operation")

"""this is our login model"""
login_model = login_api.model("Login", {
    "email": fields.String(required=True, description="user's email"),
    "password": fields.String(required=True, description="user's password")
})

"""this route is created for authetication of user upon login"""
@login_api.route("/login")
class Login(Resource):
    login_api.expect(login_model)
    def post(self):
        credentials= login_api.payload
        user = facade.get_user_by_email(credentials['email'])
        if not user or not user.verify_password(credentials["password"]):
            return {"error": "Invalid email or password."}, 401
        access_token = create_access_token(identity={"id": str(user.id), "is_admin": user.is_admin})
        return {"access_token":access_token}, 200

"""this endpoint was created for verification of token to grant user
access to account details and for managing of queries"""
@login_api.route("/protected")
class Protected(Resource):
    @jwt_required()
    def get(self):
        user = get_jwt_identity()
        return {"message": f'Hello user {user["id"]}'}, 200
