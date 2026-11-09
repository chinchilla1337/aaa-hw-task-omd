def add_attribute(records, attribute_name, function):
    """Добавляет новое поле в копию каждой записи."""
    result = []

    for record in records:
        new_record = record.copy()
        new_record[attribute_name] = function(record)
        result.append(new_record)

    return result
