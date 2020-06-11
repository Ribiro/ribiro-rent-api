from flask_restx import Namespace, fields


class Users:
    ns_user = Namespace('users', description='All user related operations')
    user = ns_user.model('userModel', {
        'username': fields.String(required=True, description='my name'),
        'phone': fields.String(required=True, description='phone number'),
        'email': fields.String(required=True, description='my email'),
        'password': fields.String(required=True, description='password')
    })



