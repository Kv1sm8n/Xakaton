import requests
from bs4 import BeautifulSoup
from back_api import create_card

url = "https://cultsakhalin.ru/events?limit=1000"

def parse():
    global url
    response = requests.get(url)

    bs = BeautifulSoup(response.text, 'html.parser')

    # Открытие локального HTML-файла
    """with open('./last_events.html', 'r', encoding='utf-8') as file:
        html_content = file.read()

    # Парсинг файла с помощью BeautifulSoup
    bs = BeautifulSoup(html_content, 'html.parser')"""

    sect = bs.find("div", "EntitiesGrid_cardsGrid__2fOLp EntitiesGrid_cardsGrid_20__1n5Q8")
    links = sect.find_all("a")

    for link in links:

        url = "https://cultsakhalin.ru" + link["href"]
        card = link.find("div")
        print(type(card))
        metatag = card.find("div", "EventCard_badge__CNhie").getText()
        card_img = "https://cultsakhalin.ru" + card.find("div", "EventCard_image__1KJnX Picture_image__3LsT8").find("picture").find("img")['srcset']
        date = card.find("div", "EventCard_info__9dU2Z").find("p", "EventCard_date__3kT5M").getText()
        name = card.find("div", "EventCard_info__9dU2Z").find("div", "EventCard_title__1eRmT").getText()
        try: 
            cost = card.find("div", "EventCard_info__9dU2Z").find("p", "EventCard_price__PtHTE").getText()
        except Exception as ex:
            cost = ''
        create_card(metatag, date, name, url, card_img, cost)
    return []
