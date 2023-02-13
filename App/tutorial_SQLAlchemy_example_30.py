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

class Book(Base):  
    __tablename__ = 'Books_10'  
    
    id_book = Column(Integer, primary_key=True)  
    title = Column(String(250), nullable=False)  
    author_id = Column(Integer, ForeignKey("Authors_10.id_author"))  
    genre = Column(String(250))
    price = Column(Integer, nullable=False)
    Author = relationship("Author") 

class Author(Base):  
    __tablename__ = 'Authors_10'  
    
    id_author = Column(Integer, primary_key=True)  
    name = Column(String(250), nullable=False)  
    book = relationship("Book") # 1 ко многим


Base.metadata.create_all(engine)   

