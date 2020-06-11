from service.userService import *


def login_user(data):
    email = data['email']
    password = data['password']
    print(data)

    if UsersModel.check_email_exists(email=email):
        if UsersModel.check_password(email, password):
            user = UsersModel.get_user_by_email(email=email)
            access = create_access_token(identity=user.id)
            refresh_token = create_refresh_token(identity=user.id)

            return jsonify({'acess_token': access, "refresh_token": refresh_token})
        else:
            return {"message": "Invalid email or password"}, 400
    else:
        return {"message": "Invalid email or password"}, 400
