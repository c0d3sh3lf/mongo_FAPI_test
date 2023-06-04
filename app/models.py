from mongoengine import Document, StringField, IntField, FloatField, DateTimeField
from datetime import datetime
from bson import ObjectId

class Items(Document):
    name = StringField(required=True)
    description = StringField(required=True)
    quantity = IntField(required=True)
    cost_price = FloatField(required=True)
    selling_price = FloatField(required=True)
    profit = FloatField(required=True)
    created_at = DateTimeField(default=datetime.utcnow)

    def __dict__(self):
        return {
            "_id": ObjectId(self.id).__str__(),
            "name": self.name,
            "description": self.description,
            "quantity": self.quantity,
            "cost_price": self.cost_price,
            "selling_price": self.selling_price,
            "profit": self.profit,
            "created_at": self.created_at
        }