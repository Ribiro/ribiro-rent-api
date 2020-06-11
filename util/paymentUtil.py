from flask_restx import Namespace, fields


class Payments:
    ns_payment = Namespace('payments', description='all payments related operations')
    payment = ns_payment.model('paymentModel', {
        'amount': fields.Integer(required=True, description=1000),
        # 'date': fields.String(required=True, description='date paid')
        'tenant_id': fields.Integer(required=True, description='tenant_id')
    })