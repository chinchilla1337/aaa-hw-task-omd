import statistics


def count_records(records):
    """Возвращает количество записей."""
    return len(records)


def mean_value(records, field):
    """Считает среднее значение поля."""
    values = [record[field] for record in records]
    return statistics.mean(values)


def median_value(records, field):
    """Считает медианное значение поля."""
    values = [record[field] for record in records]
    return statistics.median(values)


def max_value(records, field):
    """Возвращает максимальное значение поля."""
    values = [record[field] for record in records]
    return max(values)


def top_n(records, field, n, reverse=True):
    """Возвращает top-N записей по значению поля."""
    return sorted(
        records,
        key=lambda record: record[field],
        reverse=reverse
    )[:n]
