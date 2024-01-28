from sqlalchemy import create_engine, Column, String, Integer, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine(
    "postgresql://postgres:Hitman.agent47@localhost/freephonebook")
Base = declarative_base()


class PhoneBook1(Base):
    __tablename__ = "phonebook1"
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    phone_number = Column(String, unique=True)
    address = Column(Text)


Base.metadata.create_all(engine)


Session = sessionmaker(bind=engine)
session = Session()

dummy_data = [
    {
        "first_name": "Alice",
        "last_name": "Smith",
        "phone_number": "1234567890",
        "address": "123 Apple St",
    },
    {
        "first_name": "Bob",
        "last_name": "Johnson",
        "phone_number": "2345678901",
        "address": "456 Orange Ave",
    },
    {
        "first_name": "Carol",
        "last_name": "Williams",
        "phone_number": "3456789012",
        "address": "789 Banana Blvd",
    },
]

for data in dummy_data:
    new_entry = PhoneBook1(**data)
    session.add(new_entry)
