def best_score(a_dictionary):
    if a_dictionary is None:
        return None

    best_key = None
    best_value = 0

    for i in a_dictionary:
        if a_dictionary[i] > best_value:
            best_key = i
            best_value = a_dictionary[i]

    return best_key
