from model.Payments import PaymentsModel, payment_schema, payments_schema
from datetime import datetime


def get_payments():
    return payments_schema.dump(PaymentsModel.fetch_all())


def add_payment(data):
    d = datetime.now()

    month = d.month
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', ' October',
              'November', 'December']
    month = months[month - 1]
    year = d.year

    date = month + ' ' + str(year)

    # new_payment = PaymentsModel(transaction_type=, transaction_id=, amount=, balance=, date=date, tenant_id=)

    record = PaymentsModel(**data)
    record.insert_record()
    return {'message': 'payment successfully added'}, 201


def get_payment(id):
    if PaymentsModel.check_id_exists(id):
        return payment_schema.dump(PaymentsModel.fetch_by_id(id))
    else:
        return {'message': 'Id not found'}, 400


def get_payments_by_tenant_id(tenant_id):
    this_payments = PaymentsModel.fetch_by_tenant_id(tenant_id)
    print(str(this_payments))
    return payments_schema.dump(this_payments), 201

