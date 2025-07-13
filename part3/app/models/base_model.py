import uuid
from datetime import datetime
from app.extensions.extensions import db

"""this module contains a base class that
defines methods that will be inherited by our
entities: user, place, review, amenity

the methods to implement are for the following recyclable data:
entity id, entity creation(by time), entity update(by time)"""

class BaseClass(db.Model):
    __abstract__ = True #is anstract, so that a table is not made of this model
    
    id = db.Column(db.String(50), primary_key=True, defualt=lambda: str(uuid.uuid4()))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def save(self):
        """method that records the time at which it was saved"""
        self.updated_at = datetime.now()
    
    def update(self, data):
        for key, value in data.items():
            if hasattr(self, key):
                setattr(self, key, value)
        self.save() #implementation of the save method to finalize the update
    
    def to_dict(self):
        return{
            "id": self.id,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat()
        }