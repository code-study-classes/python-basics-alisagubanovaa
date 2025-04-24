def count_char_occurrences(text):
    result = {}
    for char in text.lower():
        if char.isalpha():
            result[char] = result.get(char, 0) + 1
    return result


def merge_dicts(dict1, dict2, conflict_resolver):
    result = dict1.copy()
    for key, value in dict2.items():
        if key in result:
            result[key] = conflict_resolver(key, result[key], value)
        else:
            result[key] = value
    return result


def invert_dictionary(original_dict):
    inverted = {}
    for key, value in original_dict.items():
        if value in inverted:
            if isinstance(inverted[value], list):
                inverted[value].append(key)
            else:
                inverted[value] = [inverted[value], key]
        else:
            inverted[value] = [key]
    return inverted


def dict_to_table(data_dict, columns):
    if not data_dict or not columns:
        return ""

    # Подготовка данных
    headers = [col.upper() for col in columns]
    rows = []
    max_lengths = {col: len(col) for col in columns}

    # Сбор данных и вычисление максимальных длин
    for item in data_dict.values():
        row = []
        for col in columns:
            value = str(item.get(col, "N/A"))
            row.append(value)
            max_lengths[col] = max(max_lengths[col], len(value))
        rows.append(row)

    # Форматирование заголовка
    header_line = "| " + " | ".join(
        header.ljust(max_lengths[col])
        for header, col in zip(headers, columns)
    ) + " |"

    # Форматирование разделителя
    separator = "|" + "|".join(
        "-" * (max_lengths[col] + 2)
        for col in columns
    ) + "|"

    # Форматирование строк данных
    data_lines = []
    for row in rows:
        data_line = "| " + " | ".join(
            value.ljust(max_lengths[col])
            for value, col in zip(row, columns)
        ) + " |"
        data_lines.append(data_line)

    return "\n".join([header_line, separator] + data_lines)


def deep_update(base_dict, update_dict):
    result = base_dict.copy()
    for key, value in update_dict.items():
        if (key in result
            and isinstance(result[key], dict)
            and isinstance(value, dict)):
            result[key] = deep_update(result[key], value)
        elif key in result:
            result[key] = value
    return result