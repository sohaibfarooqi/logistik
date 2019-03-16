import os
from flask import jsonify, Blueprint
from .specs import BASE_PREFIX
from ..exceptions import InsufficientStockError, OrderNotFoundError
from ..models import Order
from flasgger import swag_from

bp_order = Blueprint('custom', __name__, url_prefix=BASE_PREFIX)

@swag_from("{}/swagger/order.yml".format(os.getcwd()), validation=True)
@bp_order.route('order/<int:order_id>/fulfill')
def fulfill_order(order_id):
    status_code = 200
    response = {}

    try:
        response = Order.fulfill(order_id)
    except (InsufficientStockError, OrderNotFoundError) as err:
        status_code = 400
        response = err.to_response()

    return jsonify(response), status_code
