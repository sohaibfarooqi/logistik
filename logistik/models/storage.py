from .base import Base
from .available_skus import available_skus
from ..extentions import db


class Storage(Base):
    """
    Class definition of Storage(warehouse). Defines sku and avaiable stock.
    """
    _exclude = ('skus',)

    stock = db.Column(db.Integer, nullable=False)
    skus = db.relationship('Sku', secondary=available_skus, lazy='subquery')
