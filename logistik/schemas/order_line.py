from marshmallow import EXCLUDE, Schema, fields, post_load
from  marshmallow.validate import Range
from .base import BaseSchema

class OrderLineSchema(BaseSchema):
    """
    Class definition for OrderLine model schema.
    Fields Definition:
    ------------------
        - order_id: id of the associated order.
        - sku_id: sku of item ordered
        - quantity: quantity of the sku ordered.
    """
    class Meta:
        unknown = EXCLUDE

    order_id = fields.Integer(required=True)
    sku_id = fields.Integer(required=True)
    quantity = fields.Integer(strict=True, required=True, validate=[Range(min=1, error="Quantity must be positive")])
