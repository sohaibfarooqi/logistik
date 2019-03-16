from .base import Base
from .order_line import OrderLine
from .sku import Sku
from .storage import Storage
from ..extentions import db
from ..exceptions import InsufficientStockError, OrderNotFoundError


class Order(Base):
    """
    Class definition for Order. Contains attributes associated with order,
    `customer_name`, `order_lines`.
    """
    customer_name = db.Column(db.String, nullable=False)
    order_lines = db.relationship(
        'OrderLine', lazy=True, cascade="all, delete-orphan")

    @classmethod
    def fulfill(cls, order_id):
        """
        Method to check if a particular order can be fulfiled. To fulfil an order
        all storeages needs to be checked and number of quantity for each order line
        should suffice.

        Selecting the required data requires four join. From Order we join on OrderLine to find
        all order lines associated with Order. From OrderLine join on Sku to find all skus. From
        Sku join on storage to find the stocks in each storage.
        """
        order = cls.query.join(OrderLine, OrderLine.order_id == Order.id).join(
            Sku, OrderLine.sku_id == Sku.id).join(Storage, Sku.storages).filter(OrderLine.order_id == order_id).first()
        result = list()

        if not order:
            raise OrderNotFoundError(order_id)

        # Iterate over each order line
        for item in order.order_lines:
            warehouses = item.sku.storages
            remaining = item.quantity

            # For each sku check for all available storage
            for warehouse in warehouses:
                # If quantity orderd is greater than stock available, use all warehouse stock.
                if remaining > warehouse.stock:
                    result.append(
                        {"id": warehouse.id, "quantity": warehouse.stock})
                # Else use all remaining quantity from warehouse
                else:
                    result.append({"id": warehouse.id, "quantity": remaining})
                    remaining = 0
                    break

                remaining -= warehouse.stock

            # If all warehouses have been iterated and there
            # are still some quantity left to be fulfilled
            # Throw InsufficientStockError
            if remaining > 0:
                raise InsufficientStockError(item)

        return result
