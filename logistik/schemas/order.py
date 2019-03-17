from marshmallow import EXCLUDE, Schema, fields, post_load
from .base import BaseSchema


class OrderSchema(BaseSchema):
    """
    Class definition for Order model schema.
    Fields Definition:
    ------------------
        - customer_name: Name of customer who places the order
    """
    class Meta:
        unknown = EXCLUDE

    customer_name = fields.Str(required=True)
