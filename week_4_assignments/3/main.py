from sqlalchemy import create_engine, Column, Integer, String, Float, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import func
from db_config import SalesData, Session
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import argparse


def parse_arguments():
    """
    Parses command line arguments for e-commerce data analysis.

    Returns:
        Namespace: Parsed command line arguments.
    """
    parser = argparse.ArgumentParser(description='E-commerce Data Analysis')
    parser.add_argument('-p', '--product', type=str,
                        help='Product Name for detailed information')
    parser.add_argument('-c', '--customer', type=int,
                        help='Customer Number for detailed information')
    parser.add_argument('-r', '--report', action='store_true',
                        help='Generate sales report')
    return parser.parse_args()


def product_information(session, product_name):
    """
    Prints and plots product information including total quantity ordered
    and average price for a given product from the PostgreSQL database.

    Args:
        session (Session): The SQLAlchemy session for database connection.
        product_name (str): The name of the product.
    """
    # Query to check if product exists
    if session.query(SalesData).filter(SalesData.productName == product_name).first() is None:
        print('Product not found.')
        return

    # Query to get monthly count data
    monthly_count = session.query(
        SalesData.orderMonth,
        func.sum(SalesData.quantityOrdered).label('total_quantity'),
        func.avg(SalesData.priceEach).label('average_price')
    ).filter(SalesData.productName == product_name).group_by(SalesData.orderMonth).all()

    # Data for plotting
    months, quantities, average_prices = zip(
        *[(mc.orderMonth, mc.total_quantity, mc.average_price) for mc in monthly_count])

    # Print product summary
    print(f'Product Name: {product_name}')
    print(f'Quantity Ordered: {sum(quantities)}')
    print(f'Average Price: ${np.mean(average_prices):.2f}')

    # Plotting
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 12))

    # Plot Quantity Ordered
    ax1.plot(months, quantities, color='#005f73', marker='o')
    ax1.fill_between(months, 0, quantities, color='#005f73', alpha=0.6)
    ax1.set_facecolor('#EAF4f4')
    ax1.set_title('Monthly Quantity Ordered per Product')
    ax1.set_xlabel('Month')
    ax1.set_ylabel('Quantity Ordered')
    ax1.spines[['left', 'top']].set_visible(False)
    ax1.tick_params(length=0)
    ax1.yaxis.set_ticks_position('right')

    # Plot Average Price
    ax2.plot(months, average_prices, color='#005f73', marker='o')
    ax2.set_facecolor('#EAF4f4')
    ax2.set_title('Monthly Average Price')
    ax2.set_xlabel('Month')
    ax2.set_ylabel('Average Price ($)')
    ax2.spines[['left', 'top']].set_visible(False)
    ax2.tick_params(length=0)
    ax2.yaxis.set_ticks_position('right')

    fig.set_facecolor('#EAF4f4')
    plt.tight_layout()
    plt.show()


def customer_information(session, customer_number):
    """
    Prints and plots customer information including total quantity ordered
    and final payment for a given customer from the PostgreSQL database.

    Args:
        session (Session): The SQLAlchemy session for database connection.
        customer_number (int): The customer number.
    """
    # Query to check if customer exists
    if session.query(SalesData).filter(SalesData.customerNumber == customer_number).first() is None:
        print('Customer not found.')
        return

    # Query to get monthly purchase data
    monthly_purchase = session.query(
        SalesData.orderMonth,
        func.sum(SalesData.quantityOrdered).label('total_quantity'),
        func.sum(SalesData.final_payment).label('total_payment')
    ).filter(SalesData.customerNumber == customer_number).group_by(SalesData.orderMonth).all()

    # Query to get quantity ordered by product
    monthly_customer_purchase = session.query(
        SalesData.productName,
        func.sum(SalesData.quantityOrdered).label('quantity_ordered')
    ).filter(SalesData.customerNumber == customer_number).group_by(SalesData.productName).all()

    # Data for plotting
    months, total_payments, total_quantities = zip(
        *[(mp.orderMonth, mp.total_payment, mp.total_quantity) for mp in monthly_purchase])
    products, quantities = zip(
        *[(mcp.productName, mcp.quantity_ordered) for mcp in monthly_customer_purchase])

    # Print customer summary
    print(f'Customer Number: {customer_number}')
    print(f'Total Quantity Ordered: {sum(total_quantities)}')
    print(f'Total Payment: ${sum(total_payments):.2f}')

    # Plotting
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 12))

    # Plot Total Payment
    ax1.plot(months, total_payments, color='#005f73', marker='o')
    ax1.set_facecolor('#EAF4f4')
    ax1.set_title('Monthly Total Payments')
    ax1.set_xlabel('Month')
    ax1.set_ylabel('Total Payment ($)')
    ax1.spines[['left', 'top']].set_visible(False)
    ax1.tick_params(length=0)
    ax1.yaxis.set_ticks_position('right')

    # Plot Quantity Ordered by Product
    ax2.bar(products, quantities, color='#005f73')
    ax2.set_facecolor('#EAF4f4')
    ax2.set_title('Quantity Ordered by Product')
    ax2.set_xlabel('Product Name')
    ax2.set_ylabel('Quantity Ordered')
    ax2.spines[['left', 'top']].set_visible(False)
    ax2.tick_params(length=0)
    ax2.tick_params(axis='x', rotation=90)
    ax2.yaxis.set_ticks_position('right')

    fig.set_facecolor('#EAF4f4')
    plt.tight_layout()
    plt.show()


def report(session):
    """
    Generates and plots a report of the top 5 selling products from the PostgreSQL database.

    Args:
        session (Session): The SQLAlchemy session for database connection.
    """
    # Query to get top 5 products by final payment
    top_products = session.query(
        SalesData.productName,
        func.sum(SalesData.final_payment).label('total_payment')
    ).group_by(SalesData.productName).order_by(func.sum(SalesData.final_payment).desc()).limit(5).all()

    top_product_names = [product.productName for product in top_products]

    # Query to get monthly data for top 5 products
    filtered_data_product = session.query(
        SalesData.productName,
        SalesData.orderMonth,
        func.sum(SalesData.quantityOrdered).label('quantity_ordered'),
        func.sum(SalesData.final_payment).label('total_payment')
    ).filter(SalesData.productName.in_(top_product_names)).group_by(SalesData.productName, SalesData.orderMonth).all()

    # Data for plotting
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 12))

    # Plot Quantity Ordered for Top 5 Products
    for product in top_product_names:
        product_data = [
            data for data in filtered_data_product if data.productName == product]
        months = [data.orderMonth for data in product_data]
        quantities = [data.quantity_ordered for data in product_data]
        ax1.plot(months, quantities, label=product)

    ax1.spines[['left', 'top']].set_visible(False)
    ax1.tick_params(length=0)
    ax1.set_facecolor('#EAF4f4')
    ax1.yaxis.set_ticks_position('right')
    ax1.set_xlabel('Month')
    ax1.set_ylabel('Quantity Ordered')
    ax1.set_title('5 Most Sold Products')
    ax1.legend()

    # Plot Final Payment for Top 5 Products
    for product in top_product_names:
        product_data = [
            data for data in filtered_data_product if data.productName == product]
        months = [data.orderMonth for data in product_data]
        payments = [data.total_payment for data in product_data]
        ax2.plot(months, payments, label=product)

    ax2.spines[['left', 'top']].set_visible(False)
    ax2.tick_params(length=0)
    ax2.set_facecolor('#EAF4f4')
    ax2.yaxis.set_ticks_position('right')
    ax2.set_xlabel('Month')
    ax2.set_ylabel('Sum of Payments')
    ax2.set_title('5 Most Sold Products')
    ax2.legend()

    fig.set_facecolor('#EAF4f4')
    plt.tight_layout()
    plt.show()


def load_csv_to_db(session, csv_file_path):
    """
    Loads data from a CSV file to the PostgreSQL database.

    Args:
        session: SQLAlchemy session for database connection.
        csv_file_path (str): Path to the CSV file.
    """
    # Read CSV file
    df = pd.read_csv(csv_file_path)

    # Iterate over DataFrame and insert data
    for index, row in df.iterrows():
        record = SalesData(
            productName=row['productName'],
            orderMonth=row['orderMonth'],
            priceEach=row['priceEach'],
            quantityOrdered=row['quantityOrdered'],
            final_payment=row['final_payment']
        )
        session.add(record)

    session.commit()


def main():
    """
    Main function to execute the script based on command line arguments.
    """
    args = parse_arguments()

    # Start database session
    session = Session()

    if args.product:
        product_information(session, args.product)
    elif args.customer:
        customer_information(session, args.customer)
    elif args.report:
        report(session)

    session.close()
    plt.show()


if __name__ == "__main__":
    main()
