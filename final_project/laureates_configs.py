from core import create_processor
from prizes_configs import prize_processor


def process_year(date):
    """
    достаёт год из даты формата YYYY-MM-DD.
    если год неизвестен или дата отсутствует, возвращает None.
    """
    if not isinstance(date, str):
        return None

    year = date.split('-')[0]

    if year.isdigit() and int(year) > 0:
        return int(year)

    return None


# Поля, которые нужны для лауреатов-людей.
CONFIG_PERSON = {
    'id': (['id'], int),
    'name': ['knownName', 'en'],
    'gender': ['gender'],
    'birth_year': (['birth', 'date'], process_year),
    'country_birth': ['birth', 'place', 'country', 'en'],
    'country_now': ['birth', 'place', 'countryNow', 'en'],
    'prizes_relevant': (['nobelPrizes'], prize_processor())
}


# Для организаций вместо рождения берём дату и место основания.
CONFIG_ORG = {
    'id': (['id'], int),
    'name': ['orgName', 'en'],
    'founded_year': (['founded', 'date'], process_year),
    'country_founded': ['founded', 'place', 'country', 'en'],
    'country_now': ['founded', 'place', 'countryNow', 'en'],
    'prizes_relevant': (['nobelPrizes'], prize_processor())
}


def person_processor():
    """Создаёт обработчик для одного лауреата-человека."""
    return create_processor(CONFIG_PERSON)


def org_processor():
    """Создаёт обработчик для одной организации."""
    return create_processor(CONFIG_ORG)


process_person = person_processor()
process_org = org_processor()
