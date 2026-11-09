def filter_records(records, condition):
    """возвращает записи, которые удовлетворяют условию."""
    return [record for record in records if condition(record)]


def group_by_attributes(records, attributes):
    """группирует записи по одному или нескольким атрибутам."""
    groups = {}

    for record in records:
        key = tuple(record.get(attribute) for attribute in attributes)

        if key not in groups:
            groups[key] = []

        groups[key].append(record)

    return groups


def apply_aggregations(records, aggregations):
    """применяет набор агрегаций к списку записей."""
    result = {}

    for name, function in aggregations.items():
        result[name] = function(records)

    return result


def summarize_groups(records, group_attributes, aggregations):
    """группирует записи и считает агрегаты для каждой группы."""
    groups = group_by_attributes(records, group_attributes)
    result = []

    for key, group_records in groups.items():
        row = {}

        for attribute, value in zip(group_attributes, key):
            row[attribute] = value

        row.update(apply_aggregations(group_records, aggregations))
        result.append(row)

    return result


def count_missing(records):
    """считает количество пропусков в каждом поле."""
    missing = {}

    for record in records:
        for field in record:
            if field not in missing:
                missing[field] = 0

    for record in records:
        for field in missing:
            value = record.get(field)

            if value is None or value == '' or value == [] or value == {}:
                missing[field] += 1

    return missing


def calculate_missing_share(records):
    """считает долю пропусков в каждом поле в процентах."""
    if not records:
        return {}

    missing = count_missing(records)

    return {
        field: round(count / len(records) * 100, 2)
        for field, count in missing.items()
    }


def find_duplicate_values(values):
    """возвращает повторяющиеся значения без дублей в результате."""
    seen = set()
    duplicates = set()

    for value in values:
        if value in seen:
            duplicates.add(value)
        else:
            seen.add(value)

    return sorted(duplicates)


def find_gaps(values):
    """соседние уникальные значения с разницей больше единицы."""
    sorted_values = sorted(set(values))
    gaps = []

    for index in range(len(sorted_values) - 1):
        current_value = sorted_values[index]
        next_value = sorted_values[index + 1]

        if next_value - current_value > 1:
            gaps.append((current_value, next_value))

    return gaps
