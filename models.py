from sqlalchemy import Integer,Column, String,Boolean
from database import base

class TodoModel(base):
    __tablename__ = "todos"
    id = Column(Integer,primary_key=True,index = True)
    title  = Column(String(16),index=True)
    description = Column(String(16),index=True,nullable=True)
    completed = Column(Boolean,default=False)
    
    