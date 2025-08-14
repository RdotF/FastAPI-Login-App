from utilities.db_base import Base
from sqlalchemy import Column, Integer, String

class Person(Base):
    __tablename__ = 'people'
    id = Column(String, primary_key=True, index=True)
    name=Column(String)
    surname=Column(String)
    gender=Column(String)
    age=Column(Integer)

    def to_dict(self):
        """Convert the Person instance to a dictionary"""
        return {
            "id": self.id,
            "name": self.name,
            "surname": self.surname,
            "gender": self.gender,
            "age": self.age
        }