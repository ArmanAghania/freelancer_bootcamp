# Phonebook with SQLAlchemy and Peewee

This project demonstrates the creation and manipulation of a phonebook database using two popular Python ORMs: SQLAlchemy and Peewee. The project is divided into two main files, each utilizing one of these ORMs to interact with a PostgreSQL database.

## Features
* Creation of a phonebook table in PostgreSQL.
* Insertion of dummy data.
* Fetching and displaying records from the database.

## Project Structure

`phonebook_sqlalchemy.py`: Contains code for creating and interacting with the phonebook using SQLAlchemy.

`phonebook_peewee.py`: Contains code for creating and interacting with the phonebook using Peewee.

## Requirements
* PostgreSQL
* Python 3.11
* SQLAlchemy
* Peewee
* psycopg2 or psycopg2-binary

## Setup

1. Install Required Python Libraries:
    ```bash
    `pip install -r requirements.py`

2. Configure PostgreSQL:

    Ensure PostgreSQL is installed and running on your machine. Create a database named `freephonebook`.

3. Environment Setup:

    Replace the database credentials in both scripts with your PostgreSQL credentials.

## Usage

1. Running with SQLAlchemy:

    Execute the `phonebook_sqlalchemy.py` script to create the phonebook, insert data, and display the records using SQLAlchemy.
    ```bash
    `python phonebook_sqlalchemy.py`

2. Running with Peewee:

    Execute the `phonebook_peewee.py` script to create the phonebook, insert data, and display the records using Peewee.
    ```bash
    `python phonebook_peewee.py`

## How It Works
* Both scripts start by connecting to a PostgreSQL database.
* They then define a PhoneBook class/table with fields for first name, last name, phone number (unique), and address.
* Dummy data is inserted into this table.
* Finally, the inserted records are fetched and printed to the console.

## Contributing
Contributions, issues, and feature requests are welcome. Feel free to check issues page if you want to contribute.