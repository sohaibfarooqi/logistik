from functools import partial
from .base import Base
from .available_skus import available_skus
from ..extentions import db
from ..schemas import SkuSchema

class Sku(Base):
    """
    Class definition of Sku. Definies product name
    """
    _exclude = ('skus', 'storages')
    _schema_class = SkuSchema()

    product_name = db.Column(db.String, nullable=False)
    storages = db.relationship(
        'Storage', secondary=available_skus, order_by='Storage.stock', lazy='subquery')
