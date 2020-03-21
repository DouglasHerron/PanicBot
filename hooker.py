import requests
from bs4 import BeautifulSoup

def find_stats(country=None):
    if not country:
        url = "https://www.worldometers.info/coronavirus/"
    else:
        url = f"https://www.worldometers.info/coronavirus/country/{country}"

    html_doc = requests.get(url).text
    soup = BeautifulSoup(html_doc, 'html.parser')

    # number = soup.select_one(".maincounter-number span")
    numbers = soup.select(".maincounter-number span")

    if len(numbers) != 3:
        raise Exception(f"{country} not found!")

    # print(int(number.text.replace(',', '')))
    return [int(number.text.replace(',', '')) for number in numbers]