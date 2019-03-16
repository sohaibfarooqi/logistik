from flask_restless import url_for

from ..logistik.models import Order


def test_create_order(webapp):
    """
    Test create order endpoint
    """
    response = webapp.post(url_for(Order), json={'customer_name': "John Doe"})
    assert response.status_code == 201


def test_read_order(webapp):
    """
    Test fetch order endpoint
    """
    response = webapp.get(url_for(Order))
    assert response.status_code == 200


def test_update_order(webapp):
    """
    Test update order endpoint
    """
    response = webapp.get(url_for(Order)).get_json().get('objects')[0]
    response.update({"customer_name": "Alzheimer"})
    response = webapp.put("{}/{}".format(url_for(Order),
                                         response.get('id')), json=response)
    assert response.status_code == 200
    assert response.get_json().get('customer_name') == "Alzheimer"


def test_delete_order(webapp):
    """
    Test delete order endpoint
    """
    response = webapp.get(url_for(Order)).get_json().get('objects')[0]
    response = webapp.delete(
        "{}/{}".format(url_for(Order), response.get('id')))
    assert response.status_code == 204
