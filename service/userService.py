from model.Users import UsersModel, user_schema, users_schema
from main import bcrypt, create_refresh_token, create_access_token, jsonify


def get_users():
    return users_schema.dump(UsersModel.fetch_all())


def add_user(data):
    if UsersModel.check_email_exists(data['email']):
        return {'message': "Email already exist"}, 400
    else:
        username = data['username']
        email = data['email']
        password = data['password']
        phone = data['phone']

        # hashing the password
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
        record = UsersModel(username=username, email=email, password=hashed_password, phone=phone)
        item = record.insert_record()

        # creating an acess token to enable a user access a resource
        access_token = create_access_token(identity=item.id)
        # to renew an access token
        refresh_token = create_refresh_token(identity=item.id)

        return {"access_token":access_token,"refresh_token":refresh_token},200


def get_user(id):
    if UsersModel.check_id_exists(id):
        return user_schema.dump(UsersModel.fetch_by_id(id))
    else:
        return {'message': 'Id not found'}, 400


def update_user(id):
    pass


def delete_user(id):
    return UsersModel.delete_by_id(id)