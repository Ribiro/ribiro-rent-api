from model.Houses import HousesModel, house_schema, houses_schema
from main import jwt_required, get_jwt_identity, api, jsonify
from model.Users import UsersModel


def get_houses():
    user_id = get_jwt_identity()  # get a users id
    user = UsersModel.fetch_by_id(user_id)  # get the user's houses
    print(user.houses)
    return {"houses": houses_schema.dump(user.houses)}


def add_house(data):
    if HousesModel.check_house_exists(data['house_no']):
        return {'message': "House already exists"}, 400
    else:
        house_no = data['house_no']
        rent_amount = data['rent_amount']
        new_house = HousesModel(house_no=house_no, rent_amount=rent_amount, users_id=get_jwt_identity())
        new_house.insert_record()
        return house_schema.dump(new_house), 201


def get_house(id):
    if HousesModel.check_id_exists(id):
        return house_schema.dump(HousesModel.fetch_by_id(id))
    else:
        return {'message': 'Id not found'}, 400


def get_house_by_status(status):
    this_status = HousesModel.fetch_by_status(status)
    print(str(this_status))
    return houses_schema.dump(this_status), 201


# def get_house_by_house_no(house_no):
#     this_house = HousesModel.fetch_by_house_no(house_no)
#     print(str(this_house))
#     # if HousesModel.check_house_exists(house_no):
#     #     print(house_no)
#     #     return house_schema.dump(HousesModel.fetch_by_house_no(house_no))
#     # else:
#     #     return {'message': 'house not found'}, 400


def update_house(id, data):
    if HousesModel.check_id_exists(id):
        house_no = data['house_no']
        rent_amount = data['rent_amount']
        # status = data['status']
        updated_house = HousesModel.update_by_id(id=id, house_no=house_no, rent_amount=rent_amount)
        return house_schema.dump(updated_house), 201
    else:
        return {'message': 'Error in updating house'}


def delete_house(id):
    HousesModel.delete_by_id(id)
    return {"message": "House deleted successfully"}, 200