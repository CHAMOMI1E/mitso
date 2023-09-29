from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

from bs4 import BeautifulSoup


def parsing(html):
    soup = BeautifulSoup(html, 'html.parser')

    tables = soup.find_all('table')

    week_schedule = {}

    for i, table in enumerate(tables):

        date = soup.find_all('h2')[i].get_text(strip=True)

        rows = table.find_all('tr')[1:]

        schedule = []
        for row in rows:
            columns = row.find_all('td')
            time = columns[0].get_text(strip=True)
            subject_and_teacher = columns[1].get_text(strip=True)
            classroom = columns[2].get_text(strip=True)

            schedule.append({
                'Time': time,
                'Subject and Teacher': subject_and_teacher,
                'Classroom': classroom
            })
        week_schedule[date] = schedule

    for date, schedule in week_schedule.items():
        print(f"Расписание на {date}:")
        for entry in schedule:
            print(
                f"Время: {entry['Time']}, Предмет и Преподаватель: {entry['Subject and Teacher']}, Аудитория: {entry['Classroom']}")
        print()


driver = webdriver.Chrome()
time_for_request = float(0.5)
url = "https://apps.mitso.by/frontend/web/schedule/index"

try:
    driver.get(url)

    schedule_dropdown = Select(driver.find_element(By.NAME, "ScheduleSearch[fak]"))
    schedule_dropdown.select_by_visible_text("Экономический")
    time.sleep(time_for_request)
    form_dropdown = Select(driver.find_element(By.NAME, "ScheduleSearch[form]"))
    form_dropdown.select_by_visible_text("Дневная")
    time.sleep(time_for_request)
    course_dropdown = Select(driver.find_element(By.NAME, "ScheduleSearch[kurse]"))
    course_dropdown.select_by_visible_text("4 курс")
    time.sleep(time_for_request)
    group_dropdown = Select(driver.find_element(By.NAME, "ScheduleSearch[group_class]"))
    group_dropdown.select_by_visible_text("2021 ИСИТ")
    time.sleep(time_for_request)
    week_dropdown = Select(driver.find_element(By.NAME, "ScheduleSearch[week]"))
    week_dropdown.select_by_visible_text("Текущая неделя")
    time.sleep(time_for_request)

    submit_button = driver.find_element(By.XPATH, "//button[@type='submit']")
    submit_button.click()

    time.sleep(time_for_request)

    html_content = driver.page_source
    print(parsing(html_content))

except Exception as e:
    print("Ошибка:", str(e))

finally:
    driver.quit()
