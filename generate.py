"""_summary_

    Returns:
        _type_: _description_
"""

# import datetime
import calendar
from faker import Faker
from faker.providers import BaseProvider
import polars as pl


def add_one_month(orig_date):
    # advance year and month by one month
    new_year = orig_date.year
    new_month = orig_date.month + 1
    # note: in datetime.date, months go from 1 to 12
    if new_month > 12:
        new_year += 1
        new_month -= 12

    last_day_of_month = calendar.monthrange(new_year, new_month)[1]
    new_day = min(orig_date.day, last_day_of_month)

    return orig_date.replace(year=new_year, month=new_month, day=new_day)


organizations = {
        "name": [
            "Рязанский государственный университет имени С.А. Есенина (РГУ)",
            "Рязанский государственный радиотехнический университет имени В.Ф. Уткина (РГРТУ)",
            "Рязанский филиал Московского государственного университета путей сообщения Императора Николая II (МИИТ)",
            "Рязанский государственный медицинский университет имени И.П. Павлова (РязГМУ)",
            "Рязанский колледж железнодорожного транспорта",
            "Рязанский авиационный техникум",
            "Рязанский строительный колледж",
            "Рязанский колледж экономики и информатики",
            "Рязанский педагогический колледж",
            "Рязанский медицинский колледж",
            "Гимназия №1 имени К.И. Мягкова (г. Рязань)",
            "Лицей №51 (г. Рязань)",
            "Школа-интернат №2 для обучающихся с ограниченными возможностями здоровья (г. Рязань)",
            "Многопрофильный лицей №6 (г. Рязань)",
            "Гимназия №8 (г. Рязань)",
            "Средняя общеобразовательная школа №17 (г. Рязань)",
            "Кадетская школа-интернат «Рязанский кадетский корпус»",
            "Рязанский агротехнологический колледж",
            "Сасовский филиал РГРТУ (г. Сасово)",
            "Шацкий политехнический техникум (г. Шацк, Рязанская область)"
        ],
        "type": [
            "Учреждение профессионального образования",
            "Учреждение высшего образования",
            "Учреждение среднего образования",
            "Учреждение дополнитего образования",
            "Библиотека",
            "Министерство финансов",
            "Министерство труда"
        ],
}
teachers_spesiality = [
    "География",
    "Обществознание",
    "История",
    "Экономика",
]
events = {
    "title": [
        "Бюджет без стресса",
        "Кредиты: плюсы и ловушки",
        "Инвестируй с умом",
        "Финансы для подростков",
        "Пенсия начинается сегодня",
        "Страховка или переплата?",
        "Цифровые деньги — безопасно!",
        "Мошенники: как не попасться",
        "Читаем договоры правильно",
        "Семейный кошелёк"
    ],
    "type": [
        "Лекция",
        "Публичная лекция",
        "Научно-популярная лекция",
        "Семинар",
        "Просветительский семинар",
        "Вебинар",
        "Научно-популярный вебинар",
        "Мастер-класс",
        "Просветительский мастер-класс",
        "Дискуссия",
        "Круглый стол",
        "Дебаты",
        "Чтения",
        "Научные чтения",
        "Публичные чтения",
        "Кинолекторий",
        "Книжный клуб",
        "Литературная гостиная",
        "Экскурсия (образовательная)",
        "Музейный урок",
        "Научный квест",
        "Просветительская акция",
        "День науки",
        "Неделя просвещения",
        "Фестиваль науки",
        "Форум просветителей",
        "Школа для родителей",
        "Просветительский марафон",
        "Интерактивная выставка с лекциями",
        "Встреча с экспертом"
    ],
    "format": ["online", "ofline"],
    "topic": [
        "Как составить личный бюджет и не жить в долг",
        "Понимание банковских продуктов: вклады, кредиты, дебетовые и кредитные карты",
        "Как не попасться на уловки финансовых мошенников",
        "Основы инвестирования для начинающих: от копилки до фондового рынка",
        "Финансовая грамотность для подростков: карманные деньги, первые покупки, цифровые финансы",
        "Пенсия и долгосрочное планирование: как обеспечить себе будущее сегодня",
        "Страхование: что действительно нужно, а за что платить не стоит",
        "Цифровые финансы: безопасные переводы, мобильные банки, электронные кошельки",
        "Как читать финансовые документы: выписки, договоры, условия кредитов",
        "Семейная финансовая грамотность: совместный бюджет, воспитание финансовой ответственности у детей"
    ]
}

audience = {
    "age_group": [
        "Дети",
        "Школьники",
        "Студенты",
        "Взрослые",
        "Пенсионеры",
        "Все возрастные группы"
    ],
    "social_group": [
        "Трудовые коллективы",
        "Безработные",
        "Студенты",
        "Школьники"
    ]
}

infoMaterials = {
    "title": [
        "Бюджет без стресса",
        "Кредиты: плюсы и ловушки",
        "Инвестируй с умом",
        "Финансы для подростков",
        "Пенсия начинается сегодня",
        "Страховка или переплата?",
        "Цифровые деньги — безопасно!",
        "Мошенники: как не попасться",
        "Читаем договоры правильно",
        "Семейный кошелёк"
    ],
    "format": [
        "видео",
        "аудио",
        "баннер",
        "плакат",
    ],
    "type": [
        "Цифровой",
        "Печатный"
    ],
    "topic": [
        "Как составить личный бюджет и не жить в долг",
        "Понимание банковских продуктов: вклады, кредиты, дебетовые и кредитные карты",
        "Как не попасться на уловки финансовых мошенников",
        "Основы инвестирования для начинающих: от копилки до фондового рынка",
        "Финансовая грамотность для подростков: карманные деньги, первые покупки, цифровые финансы",
        "Пенсия и долгосрочное планирование: как обеспечить себе будущее сегодня",
        "Страхование: что действительно нужно, а за что платить не стоит",
        "Цифровые финансы: безопасные переводы, мобильные банки, электронные кошельки",
        "Как читать финансовые документы: выписки, договоры, условия кредитов",
        "Семейная финансовая грамотность: совместный бюджет, воспитание финансовой ответственности у детей"
    ]
}
placemnet_points = {
    "type": [
        "Оффлайн",
        "Онлайн",
    ],
}


class OrganizationProvider(BaseProvider):
    __organization = organizations

    def org_name(self):
        return self.random_element(self.__organization["name"])

    def org_type(self):
        return self.random_element(self.__organization["type"])

    def department_name(self):
        return self.random_element(["Отдел ФГ", "Экономический отдел"])


class EventProvider(BaseProvider):
    __event = events

    def event_type(self):
        return self.random_element(self.__event["type"])

    def event_format(self):
        return self.random_element(self.__event["format"])

    def event_topic(self):
        return self.random_element(self.__event["topic"])

    def event_title(self):
        return self.random_element(self.__event["title"])


class AudienceProvider(BaseProvider):
    __audience = audience

    def age_group(self):
        return self.random_element(self.__audience['age_group'])

    def social_group(self):
        return self.random_element(self.__audience['social_group'])


class IMProvider(BaseProvider):
    __info_materials = infoMaterials

    def im_type(self):
        return self.random_element(self.__info_materials['type'])

    def im_format(self):
        return self.random_element(self.__info_materials['format'])

    def im_topic(self):
        return self.random_element(self.__info_materials['topic'])

    def im_title(self):
        return self.random_element(self.__info_materials['title'])


class CustomLocationProvider(BaseProvider):
    __locations = pl.DataFrame()
    
    def __init__(self, generator):
        super().__init__(generator)
        self.__locations = pl.read_csv(
            "data/locations.csv",
            schema_overrides={"oktmo": pl.String}
            )
    
    def location(self):
        """_summary_
        Метод выбирает случайную запись из списка местоположений и возвращает 
        словарь
        Returns:
            _type_: _description_
            dict: {id:"id",	region: "region",	municipality: "municipality",
            settlement: "settlement",	type: "type",	oktmo: "oktmo"}

        """
        return self.__locations.sample(n=1, seed=45).to_dicts()[0]


class EventReportGenerator():
    record_counts = 1
    __report = {
            "settelment": [],
            "municipality": [],
            "region": [],
            "event_title": [],
            "event_type": [],
            "event_format": [],
            "event_topic": [],
            "age_group": [],
            "social_group": [],
            "arranger":  [],  # Организация организующая мероприятие
            "department": [],  # Одел в котором работают ответственные
            "person_in_charge": [],  # Ответственный за мероприятие
            "partner": [],   # Организация партнёр
            "partner_type": [],
            "volunteeres": [],
            "voluteeres_type": [],
            "Дата проведения": [],
            "Количество участников": []
        }
    fake = Faker('ru_RU')
    fake.add_provider(EventProvider)
    fake.add_provider(OrganizationProvider)
    fake.add_provider(AudienceProvider)
    fake.add_provider(CustomLocationProvider)

    def __init__(self, record_counts):
        self.record_counts = record_counts

    def generate_report(self):
        event_date = self.fake.date_between(start_date='-1y', end_date='today')
        for i in range(self.record_counts):
            self.__report["event_title"].append(self.fake.event_title())
            self.__report["event_type"].append(self.fake.event_type())
            self.__report["event_format"].append(self.fake.event_format())
            self.__report["event_topic"].append(self.fake.event_topic())
            self.__report["age_group"].append(self.fake.age_group())
            self.__report["social_group"].append(self.fake.social_group())
            self.__report["arranger"].append(self.fake.org_name())
            self.__report["department"].append(self.fake.department_name())
            self.__report["person_in_charge"].append(self.fake.name())
            self.__report["partner"].append(self.fake.org_name())
            self.__report["partner_type"].append(self.fake.org_type())
            self.__report["volunteeres"].append(
                [self.fake.name() for i in range(self.fake.random_int(1, 4))]
                )
            self.__report["voluteeres_type"].append(
                self.fake.random_element(["Лекторы", "организаторы", "Другое"])
                )
            self.__report["Дата проведения"].append(event_date)
            self.__report["Количество участников"].append(
                self.fake.random_int(30, 100))
            location = self.fake.location()
            self.__report["settelment"].append(location['settlement'])
            self.__report["municipality"].append(location['municipality'])
            self.__report["region"].append(location['region'])
        return events

    def save_report(self, filename: str = "event_report.xlsx"):
        if len(self.__report['event_title']) == 0:
            self.generate_report()
        df = pl.DataFrame(self.__report)
        df.write_excel(filename)


class CDPReportGenerator():
    __row_count = 0
    __report = {
        "Субъект РФ": [],  # region
        "ФИО": [],
        "Тип слушателя": [],
        "специализация слушателя": [],
        "место работы/учебы": [],
        "Тип места работы/учебы": [],
        "ОУ ПК": [],
        "Разработчик программы ПК": [],
        "Намиенование программы обучения": [],
        "Количество часов": [],
        "Форма обучения": [],
        "Дата начала": [],
        "Дата окончания": [],
        
    }
    fake = Faker('ru_RU')
    fake.add_provider(OrganizationProvider)
    fake.add_provider(AudienceProvider)
    fake.add_provider(CustomLocationProvider)

    def __init__(self, rowcount: int = 10) -> None: 
        self.__row_count = rowcount

    def generate_report(self):
        # if len(self.__report['ФИО']) != 0:
        #     return self.__report
        start_date = self.fake.date_between(start_date='-1y', end_date='today')
        end_date = add_one_month(start_date)
        locations = self.fake.location()
        for i in range(self.__row_count):
            self.__report["Субъект РФ"].append(locations["region"])
            self.__report["ФИО"].append(self.fake.name())
            self.__report["Тип слушателя"].append(self.fake.random_element(
                ["Педагог", "Студент", "Библиотекарь", "Соц.Служащий"]
                ))
            self.__report["специализация слушателя"].append(
                self.fake.random_element(teachers_spesiality)
                )
            self.__report["место работы/учебы"].append(self.fake.org_name())
            self.__report["Тип места работы/учебы"].append(self.fake.org_type())
            self.__report["ОУ ПК"].append(self.fake.random_element(["РИРО", "ФМЦ"]))
            self.__report["Разработчик программы ПК"].append(
                                self.fake.random_element(["РИРО", "ФМЦ"])
                                )
            self.__report["Намиенование программы обучения"].append(   
                    self.fake.random_element(
                        [
                            "Содержание и методика формирования основ финансовой грамотности детей старшего дошкольного возраста",
                            "Содержание и методика обучения финансовой грамотности в начальной школе на основе функционального подхода"
                        ]
                                             )
                    )
            self.__report["Дата начала"].append(start_date)
            self.__report["Дата окончания"].append(end_date)
            self.__report["Количество часов"].append(self.fake.random_int(10, 32))
            self.__report["Форма обучения"].append(self.fake.random_element(
                ["Очная", "Заочная", "Очно-заочная"]
                ))
        return self.__report

    def save_report(self, filename: str = "cdp_report.xlsx"):
        if len(self.__report['ФИО']) <= 0:
            self.generate_report()
        df = pl.DataFrame(self.__report)
        df.write_excel(filename)


class IMPlacementReportGenerator():
    __report = {
        "Населенный пункт": [],
        "Муниципальный р-н": [],
        "Наименование ИМ": [],
        "Тип ИМ": [],
        "Тематика ИМ": [],
        "Формат ИМ": [],
        "Наименование ТР": [],
        "Тип ТР": [],
        "URL-размещённых материалов": [],
        "Возрастная группа": [],
        "Социальная группа": [],
        "Организация": [],
        "Подразделение": [],
        "Ответственный": [],
        "Наименование партнера": [],
        "Тип партнёра": [],
        "Дата размещения": [],
        "Количество просмотров": [],
        "Количество размещённых материалов": [],
    }
    fake = Faker('ru_RU')
    fake.add_provider(OrganizationProvider)
    fake.add_provider(AudienceProvider)
    fake.add_provider(CustomLocationProvider)
    fake.add_provider(IMProvider)
    
    def __init__(self, rowcount: int = 10) -> None:
        self.__row_count = rowcount
    
    def generate_report(self):
        # if len(self.__report['Наименование ИМ']) != 0:
        #     return self.__report
        locations = self.fake.location()
        for i in range(self.__row_count):
            self.__report["Населенный пункт"].append(locations["settlement"])
            self.__report["Муниципальный р-н"].append(locations["municipality"])
            self.__report["Наименование ИМ"].append(self.fake.im_title())
            self.__report["Тип ИМ"].append(self.fake.im_type())
            self.__report["Тематика ИМ"].append(self.fake.im_topic())
            self.__report["Формат ИМ"].append(self.fake.im_format())
            self.__report["Наименование ТР"].append(self.fake.org_name())
            self.__report["Тип ТР"].append(self.fake.random_element(
                ["Оффлайн", "Онлайн"]
            ))
            self.__report["URL-размещённых материалов"].append(
                self.fake.random_element(
                    [
                        "https://www.youtube.com/watch?v=XXX",
                        "https://www.youtube.com/watch?v=YYY",
                        "https://www.youtube.com/watch?v=ZZZ",
                    ])
            )
            self.__report["Возрастная группа"].append(self.fake.age_group())
            self.__report["Социальная группа"].append(self.fake.social_group())
            self.__report["Организация"].append(self.fake.org_name())
            self.__report["Подразделение"].append(self.fake.department_name())
            self.__report["Ответственный"].append(self.fake.name())
            self.__report["Наименование партнера"].append(self.fake.org_name())
            self.__report["Тип партнёра"].append(self.fake.org_type())
            self.__report["Дата размещения"].append(
                self.fake.date_between(start_date='-1y', end_date='today')
            )
            self.__report["Количество просмотров"].append(
                self.fake.random_int(100, 1000)
            )
            self.__report["Количество размещённых материалов"].append(
                self.fake.random_int(1, 10)
            )
        return self.__report
    
    def save_report(self, filename: str = "imp_report.xlsx"):
        if len(self.__report['Наименование ИМ']) <= 0:
            self.generate_report()
        df = pl.DataFrame(self.__report)
        df.write_excel(filename)


class EduIntegrationReport():
    __row_count = 0
    fake = Faker('ru_RU')
    fake.add_provider(OrganizationProvider)
    fake.add_provider(AudienceProvider)
    fake.add_provider(CustomLocationProvider)
       
    __report = {
        "Населенный пункт": [],
        "Муниципальный р-н": [],
        "Наиемнование ОУ": [],
        "Тип ОУ": [],
        "ПФГ Внедерена": [],
        "Образовательная программа": [],
        "количество учеников": [],
        "количество учеников по ПФГ": [],
        "количество преподавателей": [],
        "количество преподавателей по ПФГ": [],
    }

    def __init__(self, rowcount: int = 10) -> None:
        self.__row_count = rowcount
        
    def generate_report(self):
        # if len(self.__report['Наиемнование ОУ']) != 0:
        #     return self.__report
        locations = self.fake.location()
        for i in range(self.__row_count):
            self.__report["Населенный пункт"].append(locations["settlement"])
            self.__report["Муниципальный р-н"].append(locations["municipality"])
            self.__report["Наиемнование ОУ"].append(self.fake.org_name())
            self.__report["Тип ОУ"].append(self.fake.org_type())
            self.__report["ПФГ Внедерена"].append(
                self.fake.boolean(chance_of_getting_true=70)
                )
            self.__report["Образовательная программа"].append(
                self.fake.random_element(
                    ["Начальное", "Общее", "Среднее", "Профессиональное", "Высшее",]
                )
            )
            self.__report["количество учеников"].append(
                self.fake.random_int(100, 1000)
            )
            self.__report["количество учеников по ПФГ"].append(
                self.fake.random_int(100, 1000)
            )
            self.__report["количество преподавателей"].append(
                self.fake.random_int(10, 100)
            )
            self.__report["количество преподавателей по ПФГ"].append(
                self.fake.random_int(10, 100)
            )
        return self.__report
    
    def save_report(self, filename: str = "edu_report.xlsx"):
        if len(self.__report['Наиемнование ОУ']) <= 0:
            self.generate_report()
        df = pl.DataFrame(self.__report)
        df.write_excel(filename)


if __name__ == "__main__":
    edr = EduIntegrationReport(20)
    event_r = EventReportGenerator(20)
    cdp_r = CDPReportGenerator(20)
    imp_r = IMPlacementReportGenerator(20)
    for i in range(1, 5):
        event_r.generate_report()
        cdp_r.generate_report()
        imp_r.generate_report()
        edr.generate_report()
    event_r.save_report(f"./data/events/event_report_{i}.xlsx")
    cdp_r.save_report(f"./data/cdps/cdp_report_{i}.xlsx")
    imp_r.save_report(f"./data/imps/imp_report_{i}.xlsx")
    edr.save_report(f"./data/edus/edu_report_{i}.xlsx")
