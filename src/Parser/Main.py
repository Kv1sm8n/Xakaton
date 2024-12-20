import requests
from bs4 import BeautifulSoup

#url = "https://cultsakhalin.ru/"

#response = requests.get(url)

#bs = BeautifulSoup(response.text)

html = '<html><head><title>Заголовок страницы</title></head><body> текст </body></html>'

#soup_html = BeautifulSoup('<html><head><title>Заголовок страницы</title></head><body></body></html>', 'html.parser')

#sect = bs.find("section", "IndexPage_section__2ATJp")


#html_file = open('test.html', "w", encoding="utf-8")

#html_file.writelines(soup_html.prettify())

def change_html_tag(html: str, container: str, tag: str = "<body>") -> str: 
    alt_tag = tag.replace('<', '</')
    html.replace(html[html.index(tag) + len(tag):html.index(alt_tag)], html[html.index(tag) + len(tag):html.index(alt_tag)] + container)
    return html

print(change_html_tag(html, 'сосите хуй негры'))