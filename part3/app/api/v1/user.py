from flask_restx import Resource, Namespace, fields, marshal_with, marshal
from flask_jwt_extended import get_jwt_identity, jwt_required, get_jwt
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

user_output_model = user_api.model("UserOutputModel", {
    "id": fields.String,
    "first_name": fields.String,
    "last_name": fields.String,
    "email": fields.String,
    "is_admin": fields.Boolean,
    "created_at":fields.DateTime,
    "updated_at": fields.DateTime
})

#now removing fields email and password, cannot be updated
user_update_model = user_api.model("UserUpdate", {
    "first_name": fields.String(),
    "last_name": fields.String(),
    "is_admin": fields.Boolean()
})

@user_api.route("/")
class UserList(Resource):
    @user_api.expect(user_model, validate=True)
    @user_api.response(201, "User creation success")
    @user_api.response(400, "Email already registered to existing user")
    @user_api.response(400, "Invalid email entered")
    @user_api.response(400, 'Invalid password')
    @marshal_with(user_output_model)
    def post(self):
        user_data = user_api.payload

        try:
            new_user = facade.create_user(user_data)
            return new_user, 201
        except ValueError as e:
            return {"error": str(e)}, 400
    
    @user_api.expect(200, "Users retrieved successfully")
    @marshal_with(user_output_model)
    def get(self):
        user_list = facade.get_all_users()
        user_data = [users.to_dict() for users in user_list] #update to remove to_dict on users
        return user_data, 200

@user_api.route("/login")
class UserLogin(Resource):
    @user_api.expect(user_login_model, validate=True)
    @user_api.response(200, "Login successful")
    @user_api.response(401, "Invalid user or email")
    def post(self):
        data = user_api.payload
        email = data.get("email")
        user = facade.get_user_by_email(email)

        if not user:
            return {"error": "User not found"}, 404
        if not user.verify_password(data["password"]):
            return {"error": "Invalid password"}, 401
        return marshal(user, user_output_model), 200

@user_api.route("/<string:user_id>")
class UserGet(Resource):
    @user_api.response(200, "User retrieved")
    @user_api.response(404, "User does not exist")
    @marshal_with(user_output_model)
    def get(self, user_id):
        user = facade.get_user(user_id)
        if not user:
            user_api.abort(404, "User not found")
        return user, 200 # pending to remove to_dict

    @user_api.expect(user_update_model, validate=True)
    @user_api.response(201, "User updated")
    @user_api.response(404, "User not found")
    @user_api.response(400, "Incorrect data")
    @jwt_required() #requires token authentication
    def put(self, user_id):
        user = facade.get_user(user_id)
        current_user = get_jwt_identity() #retrieval of token
        admin = get_jwt().get("is_admin", False) #gets admin from token
        if not user:
            return {"error": "User not found."}, 404
        
        #blocks updating if the user is not the current session user
        #watch behaviour and confirm the input recieved is a string
        if user.id != current_user:
            return {"message": "Unauthorized action."}, 403
        

        data = user_api.payload
        update_data = {}
        fields = ["first_name", "last_name", "email", "password", "is_admin"]
        restricted_fields = {"email", "password"}
        for key in data:
            if key not in fields:
                continue
            if not admin and key in restricted_fields: #this field now cannot be updated
                return {"message": "You cannot modify email or password"}, 403
            if key == "password":    
                update_data["password"] = user._hash_password(data["password"])
            else:
                update_data[key] = data[key]
        updated_user = facade.update_user(user_id, update_data)
        return updated_user.to_dict(), 200 # pending to remove to_dict
    