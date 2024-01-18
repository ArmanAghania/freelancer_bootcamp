# Dependencies
import pandas as pd
import argparse
import json
import os

# Report file as database to save reports
REPORT_FILE = 'report.json'

# Function to load reports from file


def load_report():
    if os.path.exists(REPORT_FILE):
        with open(REPORT_FILE, 'r') as file:
            return json.load(file)
    return {}

# Function to save the report to the JSON file


def save_report(report):
    with open(REPORT_FILE, 'w') as file:
        json.dump(report, file, indent=4)

# Function to Pritn Country Information


def print_country_info(df, country):
    country_info = df[df['country'] == country]

    if not country_info.empty:
        print(country_info.to_string(index=False))
    else:
        print(f'کشور {country} یافت نشد')

# Function to Update and Print Report


def update_and_print_report(country, report):
    report[country] = report.get(country, 0) + 1
    save_report(report)
    for country, count in report.items():
        print(f'{country}: {count}')


def main():
    parser = argparse.ArgumentParser(
        description='Process country names and report.')
    parser.add_argument('country', type=str, nargs='?',
                        help='Name of the country')
    parser.add_argument('-r', '--report', action='store_true',
                        help='Print report of requests')
    args = parser.parse_args()

    df = pd.read_csv('cleaned_data.csv')

    report = load_report()

    if args.country:
        print_country_info(df, args.country)
        update_and_print_report(args.country, report)
    elif args.report:
        for country, count in report.items():
            print(f'{country}: {count}')


if __name__ == '__main__':
    main()
