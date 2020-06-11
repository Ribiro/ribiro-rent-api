from flask import Flask, Blueprint, jsonify
from flask_restx import Api
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_bcrypt import Bcrypt
from flask_cors import CORS
from flask_jwt_extended import JWTManager, create_access_token,jwt_required,get_jwt_identity, create_refresh_token
from config.config import Development, Production


app = Flask(__name__)
# app.config.from_object(Development)
app.config.from_object(Production)

authorizations = {
    'apikey': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'Authorization',
        'description': "Type in the *'Value'* input box below: **'Bearer &lt;JWT&gt;'**, where JWT is the token"
    }
}

# instance of bcrypt
bcrypt = Bcrypt(app)

# swagger route kind of thing
blueprint = Blueprint('rentApi', __name__, url_prefix='/api/v1')

db = SQLAlchemy(app)
ma = Marshmallow(app)
jwt=JWTManager(app)
CORS(app)


api = Api(blueprint, title='Rent Api', description='This is a rent management api', version='1.0', author='Dennis',
          contact_email='ribirodenis05@gmail.com', doc='/doc')
app.register_blueprint(blueprint)


from controller.houseController import ns_house
from controller.tenantController import ns_tenant
from controller.paymentController import ns_payment
from controller.userController import ns_user
from controller.login import ns_auth

from model.Houses import *
from model.Payments import *
from model.Tenants import *
from model.Users import *


# create tables in our database
@app.before_first_request
def create_tables():
    db.create_all()


api.add_namespace(ns_auth)
api.add_namespace(ns_user)
api.add_namespace(ns_house)
api.add_namespace(ns_tenant)
api.add_namespace(ns_payment)
