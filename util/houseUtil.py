from flask_restx import Namespace, fields


class Houses:
    ns_house = Namespace('houses', description='all house related operations')
    house = ns_house.model('houseModel', {
        'house_no': fields.String(required=True, description='number'),
        'rent_amount': fields.Integer(required=True, description=1000),
        # 'status': fields.String(required=True, description='vacant')
    })