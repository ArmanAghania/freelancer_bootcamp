import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
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


def product_information(df, product_name):
    """
    Prints and plots product information including total quantity ordered
    and average price for a given product.

    Args:
        df (DataFrame): The e-commerce dataset.
        product_name (str): The name of the product.
    """
    # Group by product and month, then calculate sum and mean
    monthly_count = df.groupby(['productName', 'orderMonth']).agg(
        {'quantityOrdered': 'sum', 'priceEach': 'mean'}).reset_index()

    if product_name in df['productName'].unique():
        # Print product summary
        print(f'Product Name: {product_name}')
        print(
            f'Quantity Ordered: {monthly_count[monthly_count["productName"] == product_name]["quantityOrdered"].sum()}')
        print(
            f'Average Price: ${monthly_count[monthly_count["productName"] == product_name]["priceEach"].mean():.2f}')

        # Plotting
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 12))
        product_data = monthly_count[monthly_count['productName']
                                     == product_name]

        # Plot Quantity Ordered
        ax1.plot(product_data['orderMonth'],
                 product_data['quantityOrdered'], color='#005f73', marker='o')
        ax1.fill_between(
            product_data['orderMonth'], 0, product_data['quantityOrdered'], color='#005f73', alpha=0.6)
        ax1.set_facecolor('#EAF4f4')
        ax1.set_title('Monthly Quantity Ordered per Product')
        ax1.set_xlabel('Month')
        ax1.set_ylabel('Quantity Ordered')
        ax1.spines[['left', 'top']].set_visible(False)
        ax1.tick_params(length=0)
        ax1.yaxis.set_ticks_position('right')

        # Plot Average Price
        ax2.plot(product_data['orderMonth'],
                 product_data['priceEach'], color='#005f73', marker='o')
        ax2.set_facecolor('#EAF4f4')
        ax2.set_title('Monthly Price Average')
        ax2.set_xlabel('Month')
        ax2.set_ylabel('Average Price ($)')
        ax2.spines[['left', 'top']].set_visible(False)
        ax2.tick_params(length=0)
        ax2.yaxis.set_ticks_position('right')

        fig.set_facecolor('#EAF4f4')
    else:
        print('Product not found.')


def customer_information(df, customer_number):
    """
    Prints and plots customer information including total quantity ordered
    and final payment for a given customer.

    Args:
        df (DataFrame): The e-commerce dataset.
        customer_number (int): The customer number.
    """
    # Group by customer and month, then calculate sum
    monthly_purchase = df.groupby(['customerNumber', 'orderMonth']).agg(
        {'quantityOrdered': 'sum', 'final_payment': 'sum'}).reset_index()
    monthly_customer_purchase = df.groupby(['customerNumber', 'productName']).agg(
        {'quantityOrdered': 'sum'}).reset_index()

    if customer_number in df['customerNumber'].unique():
        # Print customer summary
        print(f'Customer Number: {customer_number}')
        print(
            f'Total Quantity Ordered: {monthly_purchase[monthly_purchase["customerNumber"] == customer_number]["quantityOrdered"].sum()}')
        print(
            f'Total Payment: ${monthly_purchase[monthly_purchase["customerNumber"] == customer_number]["final_payment"].sum():.2f}')

        # Plotting
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 12))

        # Plot Total Payment
        ax1.plot(monthly_purchase[monthly_purchase['customerNumber'] == customer_number]['orderMonth'],
                 monthly_purchase[monthly_purchase['customerNumber'] == customer_number]['final_payment'], color='#005f73', marker='o')
        ax1.set_facecolor('#EAF4f4')
        ax1.set_title('Monthly Quantity Ordered per Product')
        ax1.set_xlabel('Month')
        ax1.set_ylabel('Quantity Ordered')
        ax1.spines[['left', 'top']].set_visible(False)
        ax1.tick_params(length=0)
        ax1.yaxis.set_ticks_position('right')

        # Plot Quantity Ordered by Product
        customer_data = monthly_customer_purchase[monthly_customer_purchase['customerNumber'] == customer_number]
        ax2.plot(customer_data['productName'],
                 customer_data['quantityOrdered'], color='#005f73', marker='o')
        ax2.set_facecolor('#EAF4f4')
        ax2.set_title('Monthly Price Average')
        ax2.set_xlabel('Month')
        ax2.set_ylabel('Average Price ($)')
        ax2.spines[['left', 'top']].set_visible(False)
        ax2.tick_params(length=0)
        ax2.tick_params(axis='x', color='#22333b', rotation=90)
        ax2.yaxis.set_ticks_position('right')

        fig.set_facecolor('#EAF4f4')
    else:
        print('Customer not found.')


def report(df):
    """
    Generates and plots a report of the top 5 selling products.

    Args:
        df (DataFrame): The e-commerce dataset.
    """
    # Top 5 products by final payment
    filtered_products = df.groupby('productName').agg(
        {'final_payment': 'sum'}).sort_values('final_payment', ascending=False)[:5].index
    filtered_data_product = df.groupby(['productName', 'orderMonth']).agg(
        {'quantityOrdered': 'sum', 'final_payment': 'sum'}).reset_index()

    # Plotting
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 12))

    # Plot Quantity Ordered for Top 5 Products
    for product in filtered_products:
        product_data = filtered_data_product[filtered_data_product['productName'] == product]
        ax1.plot(product_data['orderMonth'], product_data['quantityOrdered'])
    ax1.spines[['left', 'top']].set_visible(False)
    ax1.tick_params(length=0)
    ax1.set_facecolor('#EAF4f4')
    ax1.yaxis.set_ticks_position('right')
    ax1.set_xlabel('Month')
    ax1.set_ylabel('Quantity Ordered')
    ax1.set_title('5 Most Sold Products')

    # Plot Final Payment for Top 5 Products
    for product in filtered_products:
        product_data = filtered_data_product[filtered_data_product['productName'] == product]
        ax2.plot(product_data['orderMonth'], product_data['final_payment'])
    ax2.spines[['left', 'top']].set_visible(False)
    ax2.tick_params(length=0)
    ax2.set_facecolor('#EAF4f4')
    ax2.yaxis.set_ticks_position('right')
    ax2.set_xlabel('Month')
    ax2.set_ylabel('Sum of Payments')
    ax2.set_title('5 Most Sold Products')

    fig.set_facecolor('#EAF4f4')


def load_data():
    """
    Loads the e-commerce dataset.

    Returns:
        DataFrame: The loaded dataset.
    """
    df = pd.read_csv('e-commerce.csv')
    return df


def main():
    """
    Main function to execute the script based on command line arguments.
    """
    args = parse_arguments()
    df = load_data()

    if args.product:
        product_information(df, args.product)
    elif args.customer:
        customer_information(df, args.customer)
    elif args.report:
        report(df)

    plt.show()


if __name__ == "__main__":
    main()
