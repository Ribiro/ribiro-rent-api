from flask_restx import Resource
from util.houseUtil import Houses

ns_house = Houses.ns_house
house_model = Houses.house


from service.houseService import *


@ns_house.route('')
class HouseList(Resource):
    @api.doc(security='apikey')
    @jwt_required
    def get(self):
        """Use this endpoint to get all houses"""
        return get_houses()

    @api.doc(security='apikey')
    @jwt_required
    @ns_house.expect(house_model)
    def post(self):
        """Use this enpoint to add a new house"""
        data = ns_house.payload

        return add_house(data)


@ns_house.route('/<int:id>')
class House(Resource):
    @api.doc(security='apikey')
    @jwt_required
    def get(self, id):
        """get a single house"""
        return get_house(id)

    @api.doc(security='apikey')
    @jwt_required
    @ns_house.expect(house_model)
    def put(self, id):
        """update a single house"""
        data = ns_house.payload
        return update_house(id, data)

    @api.doc(security='apikey')
    @jwt_required
    @ns_house.expect(house_model)
    def patch(self, id):
        """update a single house"""
        data = ns_house.payload
        return update_house(id, data)

    @api.doc(security='apikey')
    @jwt_required
    def delete(self, id):
        """delete a single house"""
        return delete_house(id)


@ns_house.route('/<string:status>')
class HouseByStatus(Resource):
    @api.doc(security='apikey')
    @jwt_required
    def get(self, status):
        """get houses by status"""
        return get_house_by_status(status)


# @ns_house.route('/<string:house_no>')
# class HouseByHouseNo(Resource):
#     @api.doc(security='apikey')
#     @jwt_required
#     def get(self, house_no):
#         """get house by house number"""
#         return get_house_by_house_no(house_no)

