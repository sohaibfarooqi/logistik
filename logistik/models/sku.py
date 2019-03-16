from .base import Base
from .available_skus import available_skus
from ..extentions import db


class Sku(Base):
    """
    Class definition of Sku. Definies product name
    """
    _exclude = ('skus', 'storages')

    product_name = db.Column(db.String, nullable=False)
    storages = db.relationship(
        'Storage', secondary=available_skus, order_by='Storage.stock', lazy='subquery')
