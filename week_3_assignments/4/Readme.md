# E-Commerce Data Analysis Tool
## Overview
This Python script provides a comprehensive analysis of e-commerce data. It allows users to retrieve specific product information, customer details, and generate sales reports. This tool is ideal for analyzing trends, customer behavior, and product performance in e-commerce datasets.

## Features
* Product Information: Get detailed information about a specific product, including total quantity ordered and average price.
* Customer Information: Retrieve data about a specific customer, such as total quantity ordered and total payments.
* Sales Report: Generate reports showcasing the most sold products and their respective sales figures.
Installation
Before running the script, ensure you have Python installed on your system. Additionally, the script requires several Python libraries, including pandas, numpy, and matplotlib. You can install these libraries using pip:


`pip install -r requirements.txt`<br>
OR<br>
`pip install pandas numpy matplotlib seaborn` 

## Usage
Run the script from the command line, providing different arguments based on the information you need:

1. For Product Information:

    `python ecom_analysis.py -p <"Product Name">` <br>
    Replace "Product Name" with the name of the product you want to inquire about.

2. For Customer Information:


    `python script_name.py -c <CustomerNumber>`<br>
    Replace "CustomerNumber" with the actual customer number.

3. For Sales Report:

    `python script_name.py -r`

## Data Format
Ensure your data is in the correct format for the script to function properly. The script expects a CSV file with specific columns like 'productName', 'customerNumber', 'orderMonth', 'quantityOrdered', 'priceEach', 'final_payment', etc.

## Contributing
Contributions to this project are welcome. Please fork the repository and submit a pull request for any enhancements.
