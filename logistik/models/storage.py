from .base import Base
from .available_skus import available_skus
from ..extentions import db
from ..schemas import StorageSchema

class Storage(Base):
    """
    Class definition of Storage(warehouse). Defines sku and avaiable stock.
    """
    _exclude = ('skus',)
    _schema_class = StorageSchema()

    stock = db.Column(db.Integer, nullable=False)
    skus = db.relationship('Sku', secondary=available_skus, lazy='subquery')
