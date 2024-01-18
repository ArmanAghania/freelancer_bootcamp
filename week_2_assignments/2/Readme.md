# Pandas And Generators

In this assignment pandas is used to import the data generated by scrapy.

After loading the data, different techniques are used to determine if data is clean or should it be cleaned. 

For the sample data extracted from `https://www.currencyremitapp.com/world-currency-symbols` no action was required because it was clean and was saved as it was.

In the next step a generator was defined to load cleaned data and generate a chunk for each row in the dataframe. 

In the end each row is printed in a beautiful way.

## How to run the file?

To run the file, type following commands in terminal:

1. `pip install requirements.txt`
2. `python assignment_2.py`