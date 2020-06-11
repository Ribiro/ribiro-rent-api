from flask_restx import Namespace, fields


class Tenants:
    ns_tenant = Namespace('tenants', description='all tenants related operations')
    tenant = ns_tenant.model('tenantModel', {
        'name': fields.String(required=True, description='tenant name'),
        'phone': fields.String(required=True, description='phone number'),
        'email': fields.String(required=True, description='email address'),
        'house_no': fields.String(required=True, description='house number')
    })