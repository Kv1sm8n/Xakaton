import requests
from bs4 import BeautifulSoup

url = "https://cultsakhalin.ru/events?limit=1000"

response = requests.get(url)

bs = BeautifulSoup(response.text, 'html.parser')

sect = bs.find("div", "EntitiesGrid_cardsGrid__2fOLp EntitiesGrid_cardsGrid_20__1n5Q8")

links = sect.find_all("a")

i = 0
for link in links:
    i += 1

    url = "https://cultsakhalin.ru" + link["href"]
    card = link.find("div")
    metatag = card.find("div", "EventCard_badge__CNhie").getText()
    card_img = "https://cultsakhalin.ru" + card.find("div", "EventCard_image__1KJnX Picture_image__3LsT8").find("picture").find("img")['srcset']
    date = card.find("div", "EventCard_info__9dU2Z").find("p", "EventCard_date__3kT5M").getText()
    name = card.find("div", "EventCard_info__9dU2Z").find("div", "EventCard_title__1eRmT").getText()

    print(f'{i}: {metatag}, {date}, {name}, {url}')
    