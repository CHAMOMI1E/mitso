import requests
from bs4 import BeautifulSoup

url = "https://apps.mitso.by/frontend/web/schedule/education"

# Опциональные параметры запроса, если они необходимы
params = {
    # Вставьте параметры запроса, если они требуются
}

try:
    # Отправка GET-запроса
    response = requests.get(url, params=params)

    # Проверка успешности запроса
    if response.status_code == 200:
        # Используем BeautifulSoup для парсинга HTML-кода
        soup = BeautifulSoup(response.content, "html.parser")

        # Здесь вы можете извлечь и обработать нужные данные из HTML-кода страницы
        # Например, расписание

        # Пример извлечения заголовка страницы
        # title = soup.title.text
        print("Заголовок страницы:", url)

        # Пример извлечения расписания (замените на свою логику)
        # schedule = soup.find("div", {"class": "schedule-container"}).text
        # print("Расписание:")
        # print(schedule)
    else:
        print("Ошибка при выполнении запроса. Статус код:", response.status_code)

except requests.exceptions.RequestException as e:
    print("Ошибка запроса:", str(e))
