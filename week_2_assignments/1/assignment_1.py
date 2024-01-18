import requests
from bs4 import BeautifulSoup
import json
import pandas as pd

# Function to extract information from the webpage


def extract_webpage_info(url):
    response = requests.get(url)

    soup = BeautifulSoup(response.content, "html.parser")

    title = soup.title.string if soup.title else "No Title Found"

    links = [a["href"] for a in soup.find_all("a", href=True)]

    headers = {}
    for i in range(1, 7):
        headers[f"h{i}"] = [h.get_text() for h in soup.find_all(f"h{i}")]

    return {"Title": title, "Links": links, "Headers": headers}


url = input("Enter the URL to scrape: ")
webpage_info = extract_webpage_info(url)

with open(
    "Session 2/Python/assignment_1/webpage_data.json", "w", encoding="utf-8"
) as file:
    json.dump(webpage_info, file, ensure_ascii=False, indent=4)


with open(
    "Session 2/Python/assignment_1/webpage_data.json", "r", encoding="utf-8"
) as file:
    data = json.load(file)

if isinstance(data, dict):
    web_df = pd.json_normalize(data)
else:
    web_df = pd.DataFrame(data)

print(web_df.head(10))
