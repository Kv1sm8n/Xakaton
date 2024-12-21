import requests
from bs4 import BeautifulSoup

url = "https://cultsakhalin.ru/events"

response = requests.get(url)

bs = BeautifulSoup(response.text, 'html.parser')

sect = bs.find("div", "EventCard_wrapper__18Uhg EventCard_white__U4AA2")

print(sect)
