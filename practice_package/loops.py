def sum_even_digits(number):
    total = 0
    for digit in str(abs(number)):
        if int(digit) % 2 == 0:
            total += int(digit)
    return total


def count_vowel_triplets(text):
    vowels = {'a', 'e', 'i', 'o', 'u', 'y'}
    count = 0
    text = text.lower()
    for i in range(len(text) - 2):
        if (text[i] in vowels and
            text[i + 1] in vowels and
            text[i + 2] in vowels):
            count += 1
    return count


def find_fibonacci_index(number):
    if number == 1:
        return 1 or 2
    a, b = 1, 1
    index = 2
    while b < number:
        a, b = b, a + b
        index += 1
    return index if b == number else -1


def remove_duplicates(string):
    if not string:
        return ""
    result = string[0]
    for char in string[1:]:
        if char != result[-1]:
            result += char
    return result
