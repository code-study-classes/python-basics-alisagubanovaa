def check_between_numbers(A, B, C):
    return (A < B < C) or (C < B < A)


def check_odd_three(number):
    return (abs(number) >= 100 and abs(number) <= 999) and number % 2 != 0


def check_unique_digits(number):
    num_str = str(abs(number))
    return len(num_str) == 3 and len(set(num_str)) == 3


def check_palindrome_number(number):
    num_str = str(abs(number))
    return num_str == num_str[::-1]


def check_ascending_digits(number):
    digits = [int(d) for d in str(abs(number))]
    return len(digits) == 3 and all(digits[i] < digits[i + 1] for i in range(2))
