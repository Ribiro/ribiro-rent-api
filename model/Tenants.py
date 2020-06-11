from main import db, ma
from model.common import CommonMethods


class TenantsModel(db.Model, CommonMethods):
    __tablename__ = 'tenants'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)
    phone = db.Column(db.String(10), nullable=False)
    email = db.Column(db.String(), nullable=False)
    house_no = db.Column(db.String(), nullable=False, unique=True)
    users_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    # create a pseudo column
    houses = db.relationship('HousesModel', backref='tenant')
    payments = db.relationship('PaymentsModel', backref='tenant')

    @classmethod
    def check_tenant_exists(cls, phone):
        record = TenantsModel.query.filter_by(phone=phone)
        if record.first():
            return True
        else:
            return False

    @classmethod
    def check_id_exists(cls, id):
        record = TenantsModel.query.filter_by(id=id)
        if record.first():
            return True
        else:
            return False

    #  fetch by id
    @classmethod
    def fetch_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    # update
    @classmethod
    def update_by_id(cls, id, name=None, phone=None, email=None, house_no=None):
        record = cls.query.filter_by(id=id).first()
        if record:
            if name:
                record.name = name
            if phone:
                record.phone = phone
            if email:
                record.email = email
            if house_no:
                record.house_no = house_no
            db.session.commit()
        return cls.query.filter_by(id=id).first()

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


class TenantSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'phone', 'email', 'house_no')


tenant_schema = TenantSchema()
tenants_schema = TenantSchema(many=True)