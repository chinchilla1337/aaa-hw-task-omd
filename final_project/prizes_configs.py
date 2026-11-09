from core import create_processor


CONFIG_PRIZE = {
    'prize_amount': ['prizeAmount'],
    'prize_amount_adjusted': ['prizeAmountAdjusted'],
    'award_year': (['awardYear'], int),
    'category_en': ['category', 'en'],
    'prize_status': ['prizeStatus']
}


def prize_processor():
    """
    Создаёт функцию, которая обрабатывает список премий
    по заранее заданному конфигу.
    """
    return create_processor(CONFIG_PRIZE, list_processor=True)
