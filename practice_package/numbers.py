def calculate_distance(x, y):
    return abs(x - y)


def calculate_segments(a, b):
    return a // b


def calculate_digit_sum(number):
    return sum(int(c) for c in str(abs(number)))


def round_to_multiple(number, multiple):
    if multiple == 0:
        return 0
    return multiple * round(number / multiple)


def calculate_rect_area(x1, y1, x2, y2):
    return abs((x2 - x1) * (y2 - y1))