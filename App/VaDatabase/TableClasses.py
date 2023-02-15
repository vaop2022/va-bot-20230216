from dotenv import dotenv_values
from sqlalchemy import URL, Column, ForeignKey, Integer, String  
from sqlalchemy.ext.declarative import declarative_base  
from sqlalchemy.orm import relationship  
from sqlalchemy import create_engine  

config = dotenv_values(".env")

url_object = URL.create(
        "postgresql",
        username=config.get("PG_USERNAME"),
        password=config.get("PG_PASSWORD"),
        host=config.get("PG_HOSTNAME"),
        database=config.get("PG_DATABASE"),
    )

engine = create_engine(url_object, echo = False)

Base = declarative_base()  

class VaTraceTable(Base):  
    __tablename__ = 'va_trace'  
    
    id = Column(Integer, primary_key=True)  
    chat_id = Column(String(250), nullable=False)  
    previous_action = Column(String(250))
    direction = Column(String(250))
    current_action = Column(String(250))


Base.metadata.create_all(engine)  