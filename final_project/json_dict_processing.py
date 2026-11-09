def extract_nested_value(obj, keys):
    """
    достаёт значение из вложенного словаря по списку ключей.
    если какого-то ключа нет, возвращает None.
    """
    for key in keys:
        if isinstance(obj, dict):
            obj = obj.get(key)
        elif isinstance(obj, list) and isinstance(key, int):
            if 0 <= key < len(obj):
                obj = obj[key]
            else:
                return None
        else:
            return None

    return obj


def process_dictionary_with_config(dictionary, config):
    """
    создаёт новый словарь с нужными полями.
    пути к полям и функции обработки берём из конфига.
    """
    result = {}

    for attribute, rule in config.items():
        # Если правило — кортеж, значит значение нужно обработать.
        if isinstance(rule, tuple):
            keys, func = rule
        else:
            keys = rule
            func = None

        value = extract_nested_value(dictionary, keys)

        # Пропуски не трогаем, остальные значения преобразуем.
        if value is not None and func is not None:
            value = func(value)

        result[attribute] = value

    return result


def process_list_of_dicts_with_config(list_of_dicts, config):
    """
    применяет один и тот же конфиг ко всем словарям списка.
    удобно для обработки нескольких премий одного лауреата.
    """
    if list_of_dicts is None:
        return []

    result = []

    for dictionary in list_of_dicts:
        processed = process_dictionary_with_config(dictionary, config)
        result.append(processed)

    return result


def create_processor(config, list_processor=False):
    """
    создаёт готовую функцию обработки с заданным конфигом.
    если list_processor=True, обрабатывает список словарей.
    """
    def processor(data):
        if list_processor:
            return process_list_of_dicts_with_config(data, config)

        return process_dictionary_with_config(data, config)

    return processor
