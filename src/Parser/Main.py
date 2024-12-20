import requests
from bs4 import BeautifulSoup

url = "https://cultsakhalin.ru/"

response = requests.get(url)

bs = BeautifulSoup(response.text)

sect = bs.find("section", "IndexPage_section__2ATJp")

print(sect)