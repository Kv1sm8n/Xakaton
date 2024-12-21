from flask import Flask, render_template

app = Flask(__name__)

i = 0
def create_card(metatag, date, name, url, body, cost=0):
    global i
    text_card = f'''<div class="event-card" id="card-{i}">
                <img src={url} alt={name}>
                <h2>{name}</h2>
                <p>{body}</p>
                <p class="price">Стоимость: {cost} руб.</p>
                <button class="details-button" id="detail-{i}">Подробнее</button>
                <button class="favorite-button">Добавить в избранное</button>
            </div>'''
    with open('./index.html', 'r', encoding='utf-8') as f:
        html = f.read()
    ind = html.rfind('</div>')
    html = html[:ind] + text_card + html[ind:]
    with open('./index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    i+=1

    return []

    # print(html.find('</div>'))
    # print(html[1070:])

# create_card('metatag', 'ДАТА', 'АФИША ИМЯ', 'img', 'Описание', 100)
@app.route('/')
def index():
    events = create_card('metatag', 'DATE', 'NAME', 'url', 'BODY', 'COST')  # Вызов функции при загрузке страницы
    return render_template('index.html', events=events)

if __name__ == '__main__':
    app.run(debug=True)
