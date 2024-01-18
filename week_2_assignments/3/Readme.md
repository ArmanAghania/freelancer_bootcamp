# Assignment 3
Write a code to load the previous assignment's output and get a country's name using arguments and print the related information according to following rules:

1. Input should not be case-sensitive and be able to print relevent information at all cases. 
2. If name of the mentioned country is not present in the dataframe, it should print `کشور یافت نشد`.
3. Save each input from user in a file; if the `-r`, `--reports`, arguments are passed to the file, it should print how many times each country's information was printed. For example if **Iran** was passed 5 times, it should print : `Iran: 5`

## How to run the file:
To run the file, type following commands in terminal:
1. `pip install -r requirements.txt`

2. If you want to get information about a country : <br>
`python assignment_3 [Country_name]`

3. If you want to output the report: <br>
`python assignment_3 -r` or `python assignment_3 --report`