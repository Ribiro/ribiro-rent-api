from main import db, ma
from model.common import CommonMethods


class PaymentsModel(db.Model, CommonMethods):
    __tablename__ = 'payments'
    id = db.Column(db.Integer, primary_key=True)
    transaction_type = db.Column(db.String(), nullable=False)
    transaction_id = db.Column(db.String())
    amount = db.Column(db.Integer, nullable=False)
    balance = db.Column(db.Integer, nullable=False)
    date = db.Column(db.String(), nullable=False)
    tenant_id = db.Column(db.Integer, db.ForeignKey('tenants.id'))

    @classmethod
    def check_id_exists(cls, id):
        record = PaymentsModel.query.filter_by(id=id)
        if record.first():
            return True
        else:
            return False

    #  fetch by id
    @classmethod
    def fetch_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    # fetch by tenant id
    @classmethod
    def fetch_by_tenant_id(cls, tenant_id):
        return cls.query.filter_by(tenant_id=tenant_id).all()


class PaymentSchema(ma.Schema):
    class Meta:
        fields = ('id', 'amount', 'date', 'transaction_type', 'transaction_id', 'balance', 'tenant_id')


payment_schema = PaymentSchema()
payments_schema = PaymentSchema(many=True)