def extract_file_name(full_file_name):
    return full_file_name.split('/')[-1].split('.')[0]


def encrypt_sentence(sentence):
    even = [c for i, c in enumerate(sentence) if (i + 1) % 2 == 0]
    odd = [c for i, c in enumerate(sentence) if (i + 1) % 2 != 0]
    return ''.join(even + odd[::-1])


def check_brackets(expression):
    balance = 0
    for i, char in enumerate(expression, 1):
        if char == '(':
            balance += 1
        elif char == ')':
            balance -= 1
            if balance < 0:
                return i
    return -1 if balance > 0 else 0


def reverse_domain(domain):
    return '.'.join(domain.split('.')[::-1])


def count_vowel_groups(word):
    vowels = {'a', 'e', 'i', 'o', 'u', 'y'}
    count = 0
    in_group = False
    for char in word.lower():
        if char in vowels:
            if not in_group:
                count += 1
                in_group = True
        else:
            in_group = False
    return count
