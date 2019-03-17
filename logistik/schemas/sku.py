from marshmallow import EXCLUDE, Schema, fields, post_load
from .base import BaseSchema


class SkuSchema(BaseSchema):
    """
    Class definition for Sku model schema.
    Fields Definition:
    ------------------
        - product_name: Name of the product.
    """
    class Meta:
        unknown = EXCLUDE

    product_name = fields.Str(required=True)
