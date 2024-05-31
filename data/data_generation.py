import random
import datetime
import pandas as pd

# Параметры генерации данных
num_participants = 100
num_tests = 50
num_events = 20
num_results = 200
num_participations = 150

# Функция для генерации случайной даты
def random_date(start_date, end_date):
    return start_date + datetime.timedelta(
        days=random.randint(0, int((end_date - start_date).days)))

# Функция для генерации случайного участника
def generate_participant(id):
    names = ["Иван", "Мария", "Петр", "Анна", "Сергей", "Елена"]
    genders = ["мужчина", "женщина"]
    education_levels = ["среднее", "высшее", "поствысшее", "нет образования"]
    income_levels = ["низкий", "средний", "высокий"]
    employment_statuses = ["безработный", "студент", "работающий", "пенсионер"]
    regions = ["Москва", "Санкт-Петербург", "Новосибирск", "Екатеринбург", "Казань"]

    return {
        "ID": id,
        "Имя": random.choice(names),
        "Пол": random.choice(genders),
        "Возраст": random.randint(18, 70),
        "Уровень образования": random.choice(education_levels),
        "Уровень дохода": random.choice(income_levels),
        "Занятость": random.choice(employment_statuses),
        "Регион": random.choice(regions)
    }

# Функция для генерации случайного теста
def generate_test(id):
    test_types = ["начальный", "промежуточный", "итоговый"]
    themes = ["основы финансов", "инвестирование", "кредитование", "налогообложение"]
    
    return {
        "ID": id,
        "Дата": random_date(datetime.date(2020, 1, 1), datetime.date(2023, 12, 31)),
        "Тип теста": random.choice(test_types),
        "Тематика": random.choice(themes),
        "Количество вопросов": random.randint(10, 50),
        "Средний балл": round(random.uniform(50, 100), 2),
        "Процент правильных ответов": round(random.uniform(50, 100), 2),
        "Время прохождения": random.randint(10, 60)
    }

# Функция для генерации результата тестирования
def generate_test_result(id, participants, tests):
    return {
        "ID": id,
        "Участник": random.choice(participants)["ID"],
        "Тест": random.choice(tests)["ID"],
        "Процент правильных ответов": round(random.uniform(0, 100), 2),
        "Средний балл": round(random.uniform(0, 100), 2),
        "Время прохождения": random.randint(10, 60)
    }

# Функция для генерации случайного мероприятия
def generate_event(id):
    event_types = ["семинар", "вебинар", "курс", "мастер-класс"]
    themes = ["бюджетирование", "инвестирование", "кредитование", "страхование"]
    formats = ["онлайн", "оффлайн"]
    organizers = ["государственное учреждение", "НКО", "частная организация"]
    
    return {
        "ID": id,
        "Дата": random_date(datetime.date(2020, 1, 1), datetime.date(2023, 12, 31)),
        "Тип мероприятия": random.choice(event_types),
        "Тема": random.choice(themes),
        "Формат": random.choice(formats),
        "Организатор": random.choice(organizers),
        "Длительность": random.randint(1, 8)
    }

# Функция для генерации участия в мероприятии
def generate_participation(id, participants, events):
    return {
        "ID": id,
        "Участник": random.choice(participants)["ID"],
        "Мероприятие": random.choice(events)["ID"],
        "Дата участия": random_date(datetime.date(2020, 1, 1), datetime.date(2023, 12, 31))
    }

# Генерация данных
participants = [generate_participant(i) for i in range(1, num_participants + 1)]
tests = [generate_test(i) for i in range(1, num_tests + 1)]
test_results = [generate_test_result(i, participants, tests) for i in range(1, num_results + 1)]
events = [generate_event(i) for i in range(1, num_events + 1)]
participations = [generate_participation(i, participants, events) for i in range(1, num_participations + 1)]

# Преобразование данных в DataFrame
participants_df = pd.DataFrame(participants)
tests_df = pd.DataFrame(tests)
test_results_df = pd.DataFrame(test_results)
events_df = pd.DataFrame(events)
participations_df = pd.DataFrame(participations)

# Сохранение данных в CSV файлы
participants_df.to_csv('participants.csv', index=False)
tests_df.to_csv('tests.csv', index=False)
test_results_df.to_csv('test_results.csv', index=False)
events_df.to_csv('events.csv', index=False)
participations_df.to_csv('participations.csv', index=False)

print("Данные успешно сгенерированы и сохранены в CSV файлы.")