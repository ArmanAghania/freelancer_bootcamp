# Dependencies

import pandas as pd

# Loading data from a CSV file into a Pandas DataFrame
df = pd.read_csv("output.csv")

print(df.info())

print(df.nunique())

cleaned_csv_file_path = "cleaned_data.csv"

df.to_csv("cleaned_data.csv", index=False)

# Loading  cleaned data from a CSV file into a Pandas DataFrame
cleaned_df = pd.read_csv(cleaned_csv_file_path)

# Creating a generator to load data in chunks


def load_data_generator(file_path):
    """_summary_

    Args:
        file_path (_type_): path to the csv file

    Yields:
        _type_: chunk of the csv file loaded into a Pandas DataFrame with one row in each chunk
    """

    for chunk in pd.read_csv(file_path, chunksize=1):
        yield chunk


data_generator = load_data_generator(cleaned_csv_file_path)

for row in range(len(cleaned_df)):
    data = next(data_generator)
    print(data)
