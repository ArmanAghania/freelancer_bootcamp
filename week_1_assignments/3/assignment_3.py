import requests
from bs4 import BeautifulSoup


def extract_webpage_info(url):

    # Sending a GET request to target url and saving response in a variable
    response = requests.get(url)

    # Creating soup out of request contents
    soup = BeautifulSoup(response.content, 'html.parser')

    # Extracting title from the contents
    title = soup.title.string if soup.title else "No Title Found"

    # Extracting links from contents
    links = [a['href'] for a in soup.find_all('a', href=True)]

    # Extracting headers from contents. We are using h1, h2, h3, h4, h5, h6 tags as headers.
    headers = {}
    for i in range(1, 7):
        headers[f'h{i}'] = [h.get_text() for h in soup.find_all(f'h{i}')]

    return {
        'Title': title,
        'Links': links,
        'Headers': headers
    }


url = input('Please Enter the URL to scrape: ')
webpage_info = extract_webpage_info(url)
print(webpage_info)
