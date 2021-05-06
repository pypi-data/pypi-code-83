from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sro_db.config.config import engine, session
from sro_db.model.core.models import ApplicationReference

class BaseService():
    



    def __init__(self, object):
        self.session = session
        self.object = object
        self.type = self.object.__tablename__
   

    def find_all(self):
      
        results = self.session.query(self.object).order_by(self.object.id).all()
        return results

    def get_all(self):
        
        return self.session.query(self.object).order_by(self.object.id).all()
    
    def get_by_uuid(self, uuid):
        
        return self.session.query(self.object).filter(self.object.uuid == uuid).first()
        
    def create(self, object):        
        try:
            
           
            local_object = self.session.merge(object)
            self.session.add(local_object)
            self.session.commit()            
            return local_object
        except:
            self.session.rollback() 
            raise

    def update(self, object):
        
        try:
            self.session.query(self.object).filter(self.object.id == object.id).update({column: getattr(object, column) for column in self.object.__table__.columns.keys()})
            self.session.commit()
        except:
            self.session.rollback() 
            raise

    def delete(self, object):
        self.__create_session_connection()
        try:
            self.session.delete(object)
            self.session.commit()
        except:
            self.session.rollback() 
            raise
