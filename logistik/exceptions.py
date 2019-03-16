class AppException(Exception):
  """
  Base class for exception
  """
  pass

class OrderNotFoundError(AppException):
  """
  Error raised when requested order not found in the system.
  """
  def __init__(self, order):
    self.order = order

  def to_response(self):
    return {
      "error": "Order not found",
       "order_id": self.order
    }

class InsufficientStockError(AppException):
  """
  Error raised when there is not enough quantity in
  storage to fulfill.
  """
  def __init__(self, item):
    self.item = item

  def to_response(self):
    return {
      "error": "Insufficient stock",
       "sku": self.item.sku.id,
       "product_name": self.item.sku.product_name
    }
