from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient(host='localhost', port=27017)

# Selecting the database and collection
db = client['PhoneBook']
collection = db['phonebook']

# Sample data
dummy_data = [
    {"first_name": "Alice", "last_name": "Smith",
        "phone_number": "1234567890", "address": "123 Apple St"},
    {"first_name": "Bob", "last_name": "Johnson",
        "phone_number": "2345678901", "address": "456 Orange Ave"},
    {"first_name": "Carol", "last_name": "Williams",
        "phone_number": "3456789012", "address": "789 Banana Blvd"}
]

# Inserting data
collection.insert_many(dummy_data)
