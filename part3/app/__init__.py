"""init mrthod to call and run the whole app"""
from flask import Flask
from flask_restx import Api
from app.extensions.extensions import db
from app.models.revoked_token import RevokedToken
from app.api.v1.user import user_api
from app.api.v1.amenity import amenity_api
from app.api.v1.places import place_api
from app.api.v1.review import review_api
from app.api.v1.login import auth_api
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from datetime import timedelta
from flask_migrate import Migrate

bcrypt = Bcrypt()
jwt = JWTManager()


def create_app(config_class="config.DevelopmentConfig"):
    app = Flask(__name__)
    CORS(app, supports_credentials=True, origins=['http://127.0.0.1:5500'])
    my_api = Api(app, version='1.0', title='Hbnb API', description='Hbnb Application API', url_prefix='/api/v1')
    app.config.from_object(config_class)
    app.config['JWT_TOKEN_LOCATION'] = ['headers', 'cookies']
    app.config['JWT_COOKIE_SECURE'] = False  # Set True for HTTPS only
    app.config['JWT_COOKIE_HTTPONLY'] = False #watch behaviour, change back to true
    app.config['JWT_COOKIE_SAMESITE'] = 'Lax'  # Or 'Strict' / 'None'
    app.config['JWT_ACCESS_COOKIE_PATH'] = '/'  # Optional
    app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(minutes=30)
    bcrypt.init_app(app)
    jwt.init_app(app)
    db.init_app(app)

    from app.models import revoked_token
    Migrate(app, db)
    print(db.Model.metadata.tables.keys())
    
    
    @jwt.token_in_blocklist_loader
    def check_if_token_revoked(jwt_header, jwt_payload):
        jti = jwt_payload['jti']
        return RevokedToken.is_jti_blacklisted(jti)
    
    #Placeholder for API namespace(endpoints will be added later)
    #additional namespaces for places, reviews, and ammenities will be added later
    my_api.add_namespace(user_api, path="/v1/user")
    my_api.add_namespace(amenity_api, path="/v1/amenities")
    my_api.add_namespace(place_api, path="/v1/place")
    my_api.add_namespace(review_api, path="/v1/review")
    my_api.add_namespace(auth_api, path="/v1/auth")
    for rule in app.url_map.iter_rules():
        print(f"{rule.endpoint:30s} -> {rule.rule}")
    return app