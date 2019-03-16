from flask import url_for


def test_simple_order(webapp, simple_order):
    """
    Test single item order fulfilment.
    """
    response = webapp.get(
        url_for('custom.fulfill_order', order_id=simple_order.id))
    assert response.status_code == 200

    data = response.get_json()
    quantity_sum = sum(ol.quantity for ol in simple_order.order_lines)
    assert quantity_sum == sum(warehouse.get('quantity') for warehouse in data)


def test_order_multiple_items(webapp, order_multi):
    """
    Test multiple item order fulfilment.
    """
    response = webapp.get(
        url_for('custom.fulfill_order', order_id=order_multi.id))
    assert response.status_code == 200

    data = response.get_json()
    quantity_sum = sum(ol.quantity for ol in order_multi.order_lines)
    assert quantity_sum == sum(warehouse.get('quantity') for warehouse in data)


def test_order_insufficient_stock(webapp, order_multi_error):
    """
    Test order which has one insufficient item in it.
    """
    response = webapp.get(url_for('custom.fulfill_order',
                                  order_id=order_multi_error.id))
    assert response.status_code == 400


def test_unknown_order(webapp):
    """
    Test order which doenot exist in the system.
    """
    response = webapp.get(url_for('custom.fulfill_order', order_id=0))
    assert response.status_code == 400
