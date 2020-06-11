from flask_restx import Resource
from util.userUtil import Users

ns_user = Users.ns_user
user_model = Users.user


from service.userService import *


@ns_user.route('')
class UserList(Resource):
    def get(self):
        """Use this endpoint to get all users"""
        return get_users()

    @ns_user.expect(user_model)
    def post(self):
        """Use this enpoint to add a new user"""
        data = ns_user.payload

        return add_user(data)


@ns_user.route('/<int:id>')
class User(Resource):
    def get(self, id):
        """get a single user"""
        return get_user(id)

    def put(self, id):
        """update a single user"""
        pass

    def delete(self, id):
        """delete a single user"""
        return delete_user(id)