from flask_restx import Namespace, fields


class Auth:
    ns_auth = Namespace('login', description='Use this endpoint to login')
    login_model = ns_auth.model('Login', {
        'email': fields.String(required=True, description='reading'),
        'password': fields.String(required=True, description='user password')
    })
