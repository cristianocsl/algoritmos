def my_sort(word):
    array = list(word)
    for index in range(len(array)):
        current_value = array[index]
        current_position = index
        while (
            current_position > 0
            and
            array[current_position - 1] > current_value
        ):
            array[current_position] = array[current_position - 1]
            current_position = current_position - 1
        array[current_position] = current_value
    return array


def is_anagram(first_string, second_string):
    if not (first_string and second_string):
        return False

    first_string = first_string.lower()
    second_string = second_string.lower()

    if second_string == first_string:
        return True
    else:
        return my_sort(second_string) == my_sort(first_string)
