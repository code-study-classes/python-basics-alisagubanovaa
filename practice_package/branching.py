def is_weekend(day):
    return day in {6, 7}


def get_discount(amount):
    discount = (
        0.10 * amount if amount >= 5000 else
        0.05 * amount if amount >= 1000 else
        0.0
    )
    return round(discount, 2)


def describe_number(n):
    parity = 'четное' if n % 2 == 0 else 'нечетное'
    digits = len(str(n))
    digit_words = {1: 'однозначное', 2: 'двузначное', 3: 'трехзначное'}
    return f"{parity} {digit_words[digits]} число"


def convert_to_meters(unitNumber, lengthInUnits):
    return {
        1: lambda x: x * 0.1,
        2: lambda x: x * 1000,
        3: lambda x: x * 1,
        4: lambda x: x * 0.001,
        5: lambda x: x * 0.01
    }.get(unitNumber, lambda x: 0)(lengthInUnits)


def describe_age(age):
    units = age % 10
    tens = age // 10

    units_words = {
        0: '', 1: 'один', 2: 'два', 3: 'три', 4: 'четыре',
        5: 'пять', 6: 'шесть', 7: 'семь', 8: 'восемь', 9: 'девять'
    }

    tens_words = {
        2: 'двадцать', 3: 'тридцать', 4: 'сорок',
        5: 'пятьдесят', 6: 'шестьдесят', 7: 'семьдесят',
        8: 'восемьдесят', 9: 'девяносто', 10: 'сто'
    }

    if age == 20:
        num_word = 'двадцать'
    elif age == 100:
        num_word = 'сто'
    else:
        num_word = f"{tens_words[tens]} {units_words[units]}".strip()

    if 11 <= age % 100 <= 14:
        ending = 'лет'
    else:
        ending = {
            1: 'год',
            2: 'года', 3: 'года', 4: 'года',
        }.get(units, 'лет')

    return f"{num_word} {ending}"