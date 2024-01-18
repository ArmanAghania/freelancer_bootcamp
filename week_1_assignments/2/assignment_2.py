import requests

# Taking url from user and saving it in a variable
url = input("Please Enter the URL to scrape: ")

# Sending a GET request to target url and saving response in a variable
response = requests.get(url)

print(response.status_code)  # Printing status code of the response
print(response.headers)  # Printing headers of the response
print(response.text)  # Printing text of the response
