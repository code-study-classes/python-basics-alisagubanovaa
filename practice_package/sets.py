def find_common_elements(set1, set2):
    common = set()
    for item in set1:
        if item in set2:
            common.add(item)
    return common


def is_superset(set_a, set_b):
    if not set_b:
        return True
    for item in set_b:
        if item not in set_a:
            return False
    return True


def remove_duplicates(items):
    seen = set()
    result = []
    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result


def count_unique_words(text):
    if not text.strip():
        return 0
    words = text.lower().split()
    return len(set(words))


def find_shared_items(*sets):
    if not sets:
        return set()

    common = sets[0].copy()
    for current_set in sets[1:]:
        temp = set()
        for item in common:
            if item in current_set:
                temp.add(item)
        common = temp
        if not common:
            break
    return common