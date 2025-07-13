"""this document begins a persistent database class for business rules
and database rules alike"""
from app import db
from app.models.user import User
from app.models.places import Place
from app.models.review import Review
from app.models.amenity import Amenity
from app.persistence.repository import Repository

class SQLAlchemyRepository(Repository):
    def __init__(self, model):
        self.model = model

    def add(self, obj):
        db.session.add(obj)
        db.session.commit()
    
    def get(self, obj_id):
        return self.model.query.get(obj_id)
    
    def get_all(self):
        return self.model.query.all()
    
    def update(self, obj_id, data):
        obj = self.get(obj_id)
        if obj:
            for key, value in data.items():
                if hasattr(data, obj):
                    setattr(obj, key, value)
                db.session.commit()
    
    def delete(self, obj_id):
        obj = self.get(obj_id)
        if obj:
            db.session.delete(obj)
            db.session.commit()
    
    def get_by_attribute(self, attr_name, attr_value):
        return self.model.query.filter(getattr(attr_name, attr_value) == attr_value).first()
