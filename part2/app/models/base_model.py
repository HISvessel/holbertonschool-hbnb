import uuid
from datetime import datetime

"""this module contains a base class that
defines methods that will be inherited by our
entities: user, place, review, amenity

the methods to implement are for the following recyclable data:
entity id, entity creation(by time), entity update(by time)"""

class BaseClass:
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now
        self.updated_at = datetime.now

    def save(self):
        """method that records the time at which it was saved"""
        self.updated_at = datetime.now
    
    def updated(self, data):
        for key, value in data.items:
            if hasattr(self, key):
                setattr(self, key, value)
        self.save() #implementation of the save method to finalize the update
