from sqlalchemy import create_engine, Column, Integer, String, Float, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class SalesData(Base):
    __tablename__ = 'sales_data'
    id = Column(Integer, primary_key=True)
    customerNumber = Column(Integer)
    productName = Column(String)
    orderMonth = Column(String)
    priceEach = Column(Float)
    quantityOrdered = Column(Integer)
    final_payment = Column(Float)


engine = create_engine(
    'postgresql://postgres:Hitman.agent47@localhost/phonebook')
Session = sessionmaker(bind=engine)
Base.metadata.create_all(engine)
