class AppException(Exception):
  """
  Base class for exception
  """
  pass

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
