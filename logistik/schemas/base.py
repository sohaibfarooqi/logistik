from marshmallow import EXCLUDE, Schema, fields

class BaseSchema(Schema):
    """
    Base class for all models schemas. Provides generic serialization
    and deserialization
    """
    def model_deserializer(self, data):
        return self.load(data)

