from main import db, ma
from model.common import CommonMethods


class HousesModel(db.Model, CommonMethods):
    __tablename__ = 'houses'
    id = db.Column(db.Integer, primary_key=True)
    house_no = db.Column(db.String(), nullable=False, unique=True)
    rent_amount = db.Column(db.Integer, nullable=False)
    status = db.Column(db.String(), default='vacant')
    users_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    tenants_id = db.Column(db.Integer, db.ForeignKey('tenants.id'))

    # create a pseudo column
    # payments = db.relationship('PaymentsModel', backref='house')

    @classmethod
    def check_house_exists(cls, house_no):
        record = HousesModel.query.filter_by(house_no=house_no)
        if record.first():
            return True
        else:
            return False

    @classmethod
    def check_id_exists(cls, id):
        record = HousesModel.query.filter_by(id=id)
        if record.first():
            return True
        else:
            return False

    #  fetch by id
    @classmethod
    def fetch_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    #  fetch by status
    @classmethod
    def fetch_by_status(cls, status):
        return cls.query.filter_by(status=status).all()

    #  fetch by house number
    @classmethod
    def fetch_by_house_no(cls, house_no):
        return cls.query.filter_by(house_no=house_no).first()

    # update
    @classmethod
    def update_by_id(cls, id, house_no=None, rent_amount=None, status=None):
        record = cls.query.filter_by(id=id).first()
        if record:
            if house_no:
                record.house_no = house_no
            if rent_amount:
                record.rent_amount = rent_amount
            if status:
                record.status = status
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


class HouseSchema(ma.Schema):
    class Meta:
        fields = ('id', 'house_no', 'rent_amount', 'status')


house_schema = HouseSchema()
houses_schema = HouseSchema(many=True)