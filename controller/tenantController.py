from flask_restx import Resource
from util.tenantUtil import Tenants

ns_tenant = Tenants.ns_tenant
tenant_model = Tenants.tenant


from service.tenantService import *


@ns_tenant.route('')
class TenantList(Resource):
    @api.doc(security='apikey')
    @jwt_required
    def get(self):
        """Use this endpoint to get all tenants"""
        return get_tenants()

    @api.doc(security='apikey')
    @jwt_required
    @ns_tenant.expect(tenant_model)
    def post(self):
        """Use this enpoint to add a new tenant"""
        data = ns_tenant.payload

        return add_tenant(data)


@ns_tenant.route('/<int:id>')
class Tenant(Resource):
    @api.doc(security='apikey')
    @jwt_required
    def get(self, id):
        """get a single tenant"""
        return get_tenant(id)

    @api.doc(security='apikey')
    @jwt_required
    @ns_tenant.expect(tenant_model)
    def put(self, id):
        """update a single tenant"""
        data = ns_tenant.payload
        return update_tenant(id, data)

    @api.doc(security='apikey')
    @jwt_required
    def delete(self, id):
        """delete a single tenant"""
        return delete_tenant(id)