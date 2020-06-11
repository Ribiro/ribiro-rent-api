from flask_restx import Resource
from util.login import Auth

ns_auth = Auth.ns_auth
login_model = Auth.login_model

from service.loginService import *


@ns_auth.route('')
class Login(Resource):

    @ns_auth.expect(login_model)
    def post(self):
        data = ns_auth.payload
        return login_user(data)