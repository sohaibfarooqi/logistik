from .base import Base
from ..extentions import db

class OrderLine(Base):
  """
  Class definition for OrderLine. It defines each order item,
  its associated sku and quantity
  """
  sku_id = db.Column(db.Integer, db.ForeignKey('sku.id'), nullable=False)
  sku = db.relationship('Sku', backref='orderlines')
  quantity = db.Column(db.Integer, nullable=False)
  order_id = db.Column(db.Integer, db.ForeignKey('order.id'), nullable=False)
