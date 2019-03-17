from sqlalchemy import UniqueConstraint
from .base import Base
from ..extentions import db
from ..schemas import OrderLineSchema

class OrderLine(Base):
    """
    Class definition for OrderLine. It defines each order item,
    its associated sku and quantity
    """
    _exclude = ('order', 'sku',)
    _schema_class = OrderLineSchema()

    __table_args__ = (UniqueConstraint('sku_id', 'order_id', name='_sku_order_uc'),)

    sku_id = db.Column(db.Integer, db.ForeignKey('sku.id'), nullable=False)
    sku = db.relationship('Sku')
    quantity = db.Column(db.Integer, nullable=False)
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'), nullable=False)
    order = db.relationship('Order')
