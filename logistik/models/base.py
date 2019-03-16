from ..extentions import db


class Base(db.Model):
    """
    Base class of model to add repetitive attributes and methods.
    Use this class if all your models share some common code.
    """
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=db.func.now())
    updated_at = db.Column(
        db.DateTime, default=db.func.now(), onupdate=db.func.now())

    def __repr__(self):
        """
        Generic repr implementation for debugging.
        """
        return "<{}(id={})>".format(self.__class__.__name__, self.id)
