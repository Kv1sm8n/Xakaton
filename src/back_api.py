from flask import render_template
from flask import Flask
import parser

app = Flask(__name__)

i = 0
def create_card(metatag, date, name, url, img, cost=0):
    global i
    text_card = f'''<div class="event-card" id="card-{i}">
                <img src={img} alt={name}>
                <h2>{name}</h2>
                <p class="price">{cost}</p>
                <a href="{url}"><button class="details-button" id="detail-{i}">Подробнее</button></a>
                <button class="favorite-button">Добавить в избранное</button>
                </div>'''
    with open('./templates/index.html', 'r', encoding='utf-8') as f:
        html = f.read()
    ind = html.rfind('</div>')
    html = html[:ind] + text_card + html[ind:]
    with open('./templates/index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    i+=1
    return []

@app.route('/')
def index():
    events = parser.parse()  # Вызов функции при загрузке страницы
    return render_template('index.html', events=events)

if __name__ == '__main__':
    app.run(debug=True)
