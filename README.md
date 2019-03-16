# Logistik

[![Build Status](https://travis-ci.org/sohaibfarooqi/logistik.svg?branch=master)](https://travis-ci.org/sohaibfarooqi/logistik) [![Coverage Status](https://coveralls.io/repos/github/sohaibfarooqi/logistik/badge.svg?branch=master)](https://coveralls.io/github/sohaibfarooqi/logistik?branch=master)

This app provides CRUD endpoints for logistics management. Moreover, It also provides an special endpoint
to check if an particular order can be fulfiled.

### Installation and Running
To run the app locally use following commands:

 - `git clone https://github.com/sohaibfarooqi/logistik.git`
 - `virtualenv -p python3 env`
 - `source env/bin/activate`
 - `export FLASK_APP=wsgi.py`
 - `FLASK_RUN`

At this point you will have a copy of app running locally. Access the app at `http://localhost:5000/api/v1.0/order`

### Data Model:
This app contains following entities:

  - Storage
  - Sku
  - Order
  - OrderLine

These entities are linked together with following relationships

 - A `Storage` can have `one-or-many` `Sku` and a `Sku` can be in `one-or-many` `Storage`(Many-to-Many Relationship).
 - An `Order` can have `one-or-many` `OrderLine`.(One-to-Many Relationship).
 - An `OrderLine` can have at most one `Sku` and a `Sku` can be in `one-or-many` `OrderLine`(Many-to-One Relationship).

Additionally all skus in an OrderLine must be unique.
