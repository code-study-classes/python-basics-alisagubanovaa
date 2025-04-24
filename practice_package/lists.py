def square_odds(numbers):
    return [x**2 for x in numbers if x % 2 != 0]


def normalize_names(names):
    return [name.capitalize() for name in names]


def remove_invalid_emails(emails):
    valid_emails = []
    for email in emails:
        if (
            email.count('@') == 1
            and len(email) >= 5
            and not email.startswith('@')
            and not email.endswith('@')
        ):
            valid_emails.append(email)
    return valid_emails


def filter_palindromes(words):
    return [word for word in words if word.lower() == word.lower()[::-1]]


def calculate_factorial(n):
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def find_common_prefix(strings):
    if not strings:
        return ""
    prefix = []
    for chars in zip(*strings):
        if len(set(chars)) == 1:
            prefix.append(chars[0])
        else:
            break
    return ''.join(prefix)

