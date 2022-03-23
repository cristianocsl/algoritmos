def my_sort(array):
    for index in range(len(array)):
        current_value = array[index]
        current_position = index
        while (
            current_position > 0
            and array[current_position - 1] > current_value
        ):
            array[current_position] = array[current_position - 1]
            current_position = current_position - 1
        array[current_position] = current_value
    return array


def binary_search(array, index):
    low_index = 0
    high_index = len(array) - 1
    while high_index > low_index:
        middle_index = (high_index + low_index) // 2
        if (
            array[index] == array[middle_index]
            and index != middle_index
        ):
            return array[index]

        if array[index] < array[middle_index]:
            high_index = middle_index - 1

        low_index = middle_index + 1


def find_duplicate(nums):
    sorted_nums = my_sort(nums)
    for index in range(len(sorted_nums)):
        if not isinstance(sorted_nums[index], int) or sorted_nums[index] < 0:
            return False
        if binary_search(sorted_nums, index):
            return binary_search(sorted_nums, index)
    return False
