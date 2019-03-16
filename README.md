# Logistik [![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

[![Build Status](https://travis-ci.org/sohaibfarooqi/logistik.svg?branch=master)](https://travis-ci.org/sohaibfarooqi/logistik) [![Coverage Status](https://coveralls.io/repos/github/sohaibfarooqi/logistik/badge.svg?branch=master)](https://coveralls.io/github/sohaibfarooqi/logistik?branch=master)


This app provides CRUD endpoints for logistics management. Moreover, It also provides an special endpoint
to check if an particular order can be fulfiled.

### Installation and Running
To run the app locally use following commands:

 - `git clone https://github.com/sohaibfarooqi/logistik.git`
 - `virtualenv -p python3 env`
 - `source env/bin/activate`
 - `export FLASK_APP=wsgi.py`
 - `flask db migrate`
 - `flask run`

At this point you will have a copy of app running locally. Access the app at `http://localhost:5000/api/v1.0/order`
To run test and generate coverage report use

 - pytest
 - pytest --cov=logistik tests/

To run static analyzers use:

 - bandit -r .
 - autopep8 --recursive --in-place campaign
 - isort **/*.py

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

### CRUD Api
The CRUD api is implemented using a popular open source project [Flask-Restless](https://github.com/jfinkels/flask-restless).
It provides easy and elegant REST Api for SQLAlchemy models. Using this package following endpoints are exposed for all the
models mentioned above

 - `GET /<model>`
 - `GET /<model>/id`
 - `POST /<model>`
 - `PUT /<model>/id`
 - `DELETE /<model>/id`

This package also support resource filtering. To get order based on customer name use following request:

 - `order?filter[objects]=[{"name":"customer_name","op":"like","val":"Thomas"}]`

Not only simple filtering, this package also supports SQL operators like `and`, `or`, `not` etc.

### Custom Endpoints
All custom endpoints are inside `logistik/views` directory. Currently only one endpoint i.e. `order/<order_id>/fulfill`
is present. This endpoint check if an order can be fulfiled using current stocks in storage. If order can be fulfiled it returns `storage_id` and `quantity` supplied to fulfil the order. If an order cannot be fulfiled it returns 400.

### Deployments
Continuous integration is setup on master branch using `Travis CI`. Once the build is successful, travis send the test coverage report to `Coverall` and also deploy the code to `Heroku`.

### Tech-stack used

  - Python 3.5
  - Flask
  - SQLALchemy
  - PostgreSQL
  - Gunicorn
  - Pytest
  - Swagger
  - Bandit
  - Autopep8
  - Isort

  - This app is build on Flask framework. Flask is a microframework with easy to plug third party extentions on demand.
  This makes this framework very powerful yet lightweight.
  - Datastore for this app on production is PostgreSQL. PostgreSQL is a SQL complaint database with ACID support.
  It also offers several extentions which comes very useful in special usecases e.g PostGIS, Unaccent, Ltree etc.
  - Gunicorn is a powerful production ready container for python web apps.
  - Swagger is a convenient API docs generator which is very helpful for end users to interact with.
  - Bandit is a code audit library, Autopep8 is for PEP8 adherence, Isort is to organize import files.

### Further Improvements

 - Add more test cases.
 - Create meaningful indexes for query optimization.
 - Add schema validation support with `Marshmallow`.
 - Run load test to plan capacity of system. Load testing can be done using `Apache Workbench`.
 - Package application using Docker.
 - Add authentication support to prevent unauthorized access.
 - Implement database agonistic unaccented seach. To approach this, first create a new column
   which will store the `customer_name` unaccented using python package `unicodedata`. All the search
   will be done on this column instead of original column. There is also a PostgreSQL extention `unaccent`
   which can be used in this situation. But this will create dependency on PostgreSQL and this extention search
   with ignore case.
