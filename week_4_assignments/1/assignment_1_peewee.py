from peewee import *

db = PostgresqlDatabase(
    "freephonebook", user="postgres", password="Hitman.agent47", host="127.0.0.1"
)


class BaseModel(Model):
    class Meta:
        database = db


class PhoneBook(BaseModel):
    first_name = CharField()
    last_name = CharField()
    phone_number = CharField(unique=True)
    address = TextField()


def insert_dummy_data():
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

    with db.atomic():
        for data in dummy_data:
            PhoneBook.get_or_create(**data)


def fetch_and_print_records():
    query = PhoneBook.select()
    for record in query:
        print(
            f"{record.first_name} {record.last_name}, Phone: {record.phone_number}, Address: {record.address}"
        )


db.connect()
db.create_tables([PhoneBook], safe=True)
insert_dummy_data()
fetch_and_print_records()
db.close()
