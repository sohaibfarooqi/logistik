from marshmallow import EXCLUDE, Schema, fields, post_load
from  marshmallow.validate import Range
from .base import BaseSchema
from .sku import SkuSchema

class StorageSchema(BaseSchema):
    """
    Class definition for Storage model schema.
    Fields Definition:
    ------------------
        - stock: Number of items for a sku in storage.
    """
    class Meta:
        unknown = EXCLUDE

    stock = fields.Integer(strict=True, required=True, validate=[Range(min=1, error="Stock must be positive")])
