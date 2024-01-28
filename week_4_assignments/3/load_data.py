import pandas as pd
from db_config import Session, SalesData


def load_csv_to_db(csv_file_path):
    """
    Loads data from a CSV file into the PostgreSQL database.

    Args:
        csv_file_path (str): Path to the CSV file.
    """
    session = Session()

    # Read CSV file
    df = pd.read_csv(csv_file_path)

    # Iterate over DataFrame and insert data into the database
    for index, row in df.iterrows():
        record = SalesData(
            customerNumber=row['customerNumber'],
            productName=row['productName'],
            orderMonth=row['orderMonth'],
            quantityOrdered=row['quantityOrdered'],
            priceEach=row['priceEach'],
            final_payment=row['final_payment']
        )
        session.add(record)
    session.commit()
    session.close()


csv_file_path = 'e-commerce.csv'
load_csv_to_db(csv_file_path)
