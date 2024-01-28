# MongoDB Phonebook

This project is a simple MongoDB-based phonebook application. It demonstrates the basics of using MongoDB with Python through the PyMongo driver. The application creates a phonebook database and collection, inserts sample data, and can be extended for more complex CRUD operations.

## Features

- Connection to MongoDB.
- Creation of a `phonebook` collection in the `PhoneBook` database.
- Insertion of sample contact data into the collection.

## Requirements

- MongoDB
- Python 3.11
- PyMongo

## Setup

1. **Install MongoDB**:

   Ensure MongoDB is installed and running on your machine. Refer to the [official MongoDB installation guide](https://docs.mongodb.com/manual/installation/) for instructions.

2. **Install PyMongo**:

   Install PyMongo, the Python driver for MongoDB.

   ```bash
   pip install pymongo

3. **MongoDB Server**:

    Ensure the MongoDB server is running locally on port `27017`.

## Usage

1. Running the Script:

    Execute the script to create the PhoneBook database and phonebook collection, then insert the dummy data.

    ```bash
    `python phonebook_mongodb.py`

## How It Works
* The script starts by establishing a connection to MongoDB running locally.
* It selects the PhoneBook database and the phonebook collection. If they do not exist, they will be created.
* The script then inserts a set of predefined dummy data representing phonebook entries into the collection.
* This script can be easily modified or extended for more complex database operations.

## Extending the Application
You can extend this application by adding more functionalities such as:

* Implementing CRUD (Create, Read, Update, Delete) operations.
* Adding a user interface for interacting with the phonebook.
* Implementing search functionalities based on various criteria like name, phone number, etc.

## Contributing
Contributions, issues, and feature requests are welcome. Feel free to contribute and suggest improvements.