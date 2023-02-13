from sqlalchemy import URL, Column, ForeignKey, Integer, String  
from sqlalchemy.ext.declarative import declarative_base  
from sqlalchemy.orm import relationship  
from sqlalchemy import create_engine  

hostname = 'localhost'
database = 'postgres'
username = 'postgres'
pwd = 'Postg!2408'
port_id = 5432

url_object = URL.create(
    "postgresql",
    username=username,
    password=pwd,  # plain (unescaped) text
    host=hostname,
    database=database,
)

engine = create_engine(url_object, echo = False)

Base = declarative_base()  

class VaTrace(Base):  
    __tablename__ = 'va_trace'  
    
    id = Column(Integer, primary_key=True)  
    chat_id = Column(String(250), nullable=False)    
    direction = Column(String(250))
    action = Column(String(250))


Base.metadata.create_all(engine)  