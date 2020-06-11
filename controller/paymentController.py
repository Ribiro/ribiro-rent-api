from flask_restx import Resource
from util.paymentUtil import Payments

ns_payment = Payments.ns_payment
payment_model = Payments.payment


from service.paymentService import *


@ns_payment.route('')
class PaymentList(Resource):
    def get(self):
        """Use this endpoint to get all payments"""
        return get_payments()

    @ns_payment.expect(payment_model)
    def post(self):
        """Use this enpoint to add a new payment"""
        data = ns_payment.payload

        d = datetime.now()

        month = d.month
        months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', ' October',
                  'November', 'December']
        month = months[month - 1]
        year = d.year

        date = month + ' ' + str(year)
        transaction_type = 'Payment'
        transaction_id = 'xcvshser'
        amount = data['amount']
        balance = 4000
        tenant_id = data['tenant_id']

        new_payment = PaymentsModel(transaction_type=transaction_type, transaction_id=transaction_id, amount=amount,
                                    balance=balance, date=date, tenant_id=tenant_id)

        # record = PaymentsModel(**data)
        new_payment.insert_record()
        return {'message': 'payment successfully added'}, 201

        # return add_payment(data)


# @ns_payment.route('/<int:id>')
# class Payment(Resource):
#     def get(self, id):
#         """get a single payment"""
#         return get_payment(id)


@ns_payment.route('/<int:tenant_id>')
class PaymentByTenant(Resource):
    def get(self, tenant_id):
        """get a payments by tenant id"""
        return get_payments_by_tenant_id(tenant_id)
