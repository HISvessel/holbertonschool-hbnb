"""this module creates paths for user login authentication adn authorization"""
from flask_restx import Namespace, Resource, fields
from app.services import facade
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity


"""this is our user API route model"""
auth_api = Namespace("login", description="authentication operation")

"""this is our login model"""
auth_model = auth_api.model("Login", {
    "email": fields.String(required=True, description="user's email"),
    "password": fields.String(required=True, description="user's password")
})

"""this route is created for authetication of user upon login"""
@auth_api.route("/login/")
class Login(Resource):
    auth_api.expect(auth_model)
    def post(self):
        credentials= auth_api.payload
        user = facade.get_user_by_email(credentials['email'])
        if not user or not user.verify_password(credentials["password"]):
            return {"error": "Invalid email or password."}, 401
        access_token = create_access_token(
            identity=str(user.id),
            additional_claims={"is_admin":user.is_admin,
                               "email": user.email}) #passing a string and not a dictionary
        return {"access_token": access_token}, 200

"""this endpoint was created for verification of token to grant user
access to account details and for managing of queries"""
@auth_api.route("/protected")
class Protected(Resource):
    @jwt_required()
    def get(self):
        user = get_jwt_identity()
        return {"message": f'Hello user {user["id"]}'}, 200
