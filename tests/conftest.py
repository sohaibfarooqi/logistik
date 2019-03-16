import pytest

from logistik.app import db, init_app
from logistik.models import Order, OrderLine, Sku, Storage


def create_model_obj(model, kwargs):
    """
    Helper method to create model object.
    """
    obj = model(**kwargs)
    db.session.add(obj)
    db.session.commit()
    return obj


@pytest.fixture(scope='session')
def webapp():
    """
    Flask test client fixture.
    """
    webapp = init_app()
    with webapp.app_context():
        db.create_all()
        yield webapp.test_client()


@pytest.fixture(scope="session")
def simple_order():
    """
    Fixture to create simple order i.e. 1 item and can be fulfilled.
    """
    sku = create_model_obj(Sku, {"product_name": "Pink Europhia"})
    storage = create_model_obj(Storage, {"stock": 10, "skus": [sku]})
    order = create_model_obj(Order, {"customer_name": "John Doe"})
    order_line = create_model_obj(
        OrderLine, {"order":  order, "sku": sku, "quantity": 5})

    yield order


@pytest.fixture(scope="session")
def warehouse():
    """
    Fixture to setup warehouse i.e. create skus and define storages
    """
    sku_1 = create_model_obj(Sku, {"product_name": "Pink Europhia"})
    sku_2 = create_model_obj(Sku, {"product_name": "Shokubutshu"})
    sku_3 = create_model_obj(Sku, {"product_name": "Cott 'n' Terry"})

    storage_1 = create_model_obj(Storage, {"stock": 10, "skus": [sku_1]})
    storage_2 = create_model_obj(Storage, {"stock": 1, "skus": [sku_2]})
    storage_3 = create_model_obj(Storage, {"stock": 10, "skus": [sku_2]})
    storage_4 = create_model_obj(Storage, {"stock": 3, "skus": [sku_3]})
    storage_5 = create_model_obj(Storage, {"stock": 3, "skus": [sku_3]})

    yield [sku_1, sku_2, sku_3]


@pytest.fixture(scope="session")
def order_multi(warehouse):
    """
    Fixture to setup multiple items in an order. This order can be
    fulfiled.
    """
    order = create_model_obj(Order, {"customer_name": "John Doe"})

    order_line_1 = create_model_obj(
        OrderLine, {"order": order, "sku": warehouse[0], "quantity": 5})
    order_line_2 = create_model_obj(
        OrderLine, {"order": order, "sku": warehouse[1], "quantity": 5})
    order_line_3 = create_model_obj(
        OrderLine, {"order": order, "sku": warehouse[2], "quantity": 6})

    yield order


@pytest.fixture(scope="session")
def order_multi_error(warehouse):
    """
    Fixture to setup multiple items in an order. This order can not be
    fulfiled.
    """
    order = create_model_obj(Order, {"customer_name": "John Doe"})

    order_line_1 = create_model_obj(
        OrderLine, {"order": order, "sku": warehouse[0], "quantity": 5})
    order_line_2 = create_model_obj(
        OrderLine, {"order": order, "sku": warehouse[1], "quantity": 5})
    order_line_3 = create_model_obj(
        OrderLine, {"order": order, "sku": warehouse[2], "quantity": 12})

    yield order
