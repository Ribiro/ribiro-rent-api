from model.Tenants import TenantsModel, tenant_schema, tenants_schema
from main import jwt_required, get_jwt_identity, api
from model.Users import UsersModel


def get_tenants():
    user_id = get_jwt_identity()  # get a users id
    user = UsersModel.fetch_by_id(user_id)  # get the user's tenants
    return {'tenants': tenants_schema.dump(user.tenants)}


def add_tenant(data):
    if TenantsModel.check_tenant_exists(data['phone']):
        return {'message': "Tenant with this phone already exists"}, 400
    else:
        name = data['name']
        phone = data['phone']
        email = data['email']
        house_no = data['house_no']
        tenant = TenantsModel(name=name, phone=phone, email=email, house_no=house_no, users_id=get_jwt_identity())
        new_tenant = tenant.insert_record()
        return tenant_schema.dump(new_tenant), 201


def get_tenant(id):
    if TenantsModel.check_id_exists(id):
        return tenant_schema.dump(TenantsModel.fetch_by_id(id))
    else:
        return {'message': 'Id not found'}, 400


def update_tenant(id, data):
    if TenantsModel.check_id_exists(id):
        name = data['name']
        phone = data['phone']
        email = data['email']
        house_no = data['house_no']
        updated_tenant = TenantsModel.update_by_id(id=id, name=name, phone=phone, email=email, house_no=house_no)
        return tenant_schema.dump(updated_tenant)
    else:
        return {'message': 'error in updating tenant'}


def delete_tenant(id):
    TenantsModel.delete_by_id(id)
    return {"message": "Tenant deleted successfully"}, 200