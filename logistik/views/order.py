from flask import jsonify, Blueprint
from .specs import BASE_PREFIX
from ..exceptions import InsufficientStockError
from ..models import Order

bp_order = Blueprint('custom', __name__, url_prefix=BASE_PREFIX)

@bp_order.route('order/<int:order_id>/fulfill')
def fulfill_order(order_id):
  """
  View function for order fulfillment.

  Params:
  -------
    - order_id(int): Id of order that needs to be fulfilled.

  Example Invokcation:
  --------------------
    - /api/v1.1/order/1/fulfill

  Response:
  ---------
    - [
        {
          "id": 1,
          "quantity": 5
        },
        ...
      ]
  """
  status_code = 200
  response = {}

  try:
    response = Order.fulfill(order_id)
  except InsufficientStockError as err:
    status_code = 400
    response = err.to_response()

  return jsonify(response), status_code
