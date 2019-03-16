from ..extentions import db

"""
Associative entity for many-to-many relationship between Sku and Storage model.
"""
available_skus = db.Table('available_skus',
                          db.Column('sku_id', db.Integer, db.ForeignKey(
                              'sku.id'), primary_key=True),
                          db.Column('storage_id', db.Integer, db.ForeignKey(
                              'storage.id'), primary_key=True)
                          )
