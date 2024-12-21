function toggleMenu() {
    const menuItems = document.getElementById("menu-items");
    if (menuItems.style.display === "block") {
        menuItems.style.display = "none"; // Скрыть меню
    } else {
        menuItems.style.display = "block"; // Показать меню
    }
}

function createCard(metatag, date, name, url, body, cost = 0) {
    // Создаем HTML-код карточки события
    alert("CLICK")
    const textCard = `
        <div class="event-card">
            <img src="${url}" alt="${name}">
            <h2>${name}</h2>
            <p>${body}</p>
            <p class="price">Стоимость: ${cost} руб.</p>
            <button class="details-button">Подробнее</button>
            <button class="favorite-button">Добавить в избранное</button>
        </div>
    `;

    // Находим контейнер для карточек на странице
    const eventCardsContainer = document.getElementById('event-cards');

    // Добавляем созданную карточку в контейнер
    eventCardsContainer.insertAdjacentHTML('beforeend', textCard);
}

// Пример вызова функции
// createCard('metatag', 'ДАТА', 'АФИША ИМЯ', 'https://example.com/image.jpg', 'Описание', 100);