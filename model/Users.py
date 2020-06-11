from main import db, ma, bcrypt
from model.common import CommonMethods


class UsersModel(db.Model, CommonMethods):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    phone = db.Column(db.String(10))
    email = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String())

    # create pseudo columns
    houses = db.relationship('HousesModel', backref='user')
    tenants = db.relationship('TenantsModel', backref='user')

    @classmethod
    def check_email_exists(cls, email):
        record = UsersModel.query.filter_by(email=email)
        if record.first():
            return True
        else:
            return False

    @classmethod
    def check_id_exists(cls, id):
        record = UsersModel.query.filter_by(id=id)
        if record.first():
            return True
        else:
            return False

    #  fetch by id
    @classmethod
    def fetch_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    # # update
    # @classmethod
    # def update_by_id(cls, id, name=None):
    #     record = cls.query.filter_by(id=id).first()
    #     if record:
    #         if name:
    #             record.name = name
    #         db.session.commit()
    #     return cls.query.filter_by(id=id).first()

    # delete record
    @classmethod
    def delete_by_id(cls, id):
        record = cls.query.filter_by(id=id)
        if record.first():
            record.delete()
            db.session.commit()
            return True
        else:
            return False

    # checking if the password entered and the password in the database match
    @classmethod
    def check_password(cls, email, password):
        record = UsersModel.query.filter_by(email=email).first()

        if record and bcrypt.check_password_hash(record.password, password):
            return True
        else:
            return False

    # get user by the email
    @classmethod
    def get_user_by_email(cls, email):
        return cls.query.filter_by(email=email).first()


class UserSchema(ma.Schema):
    class Meta:
        fields = ('id', 'username', 'phone', 'email')


user_schema = UserSchema()
users_schema = UserSchema(many=True)