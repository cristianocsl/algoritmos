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


def binary_search(ordered_nums, index):
    low_index = 0
    high_index = len(ordered_nums) - 1
    while high_index > low_index:
        middle_index = (high_index + low_index) // 2
        if (
            ordered_nums[index] == ordered_nums[middle_index]
            and index != middle_index
        ):
            return ordered_nums[index]

        if ordered_nums[index] < ordered_nums[middle_index]:
            high_index = middle_index - 1
        else:
            low_index = middle_index + 1
    return False


def find_duplicate(nums):
    ordered_nums = my_sort(nums)
    for index in range(len(ordered_nums)):
        if not isinstance(ordered_nums[index], int) or ordered_nums[index] < 0:
            return False
        if binary_search(ordered_nums, index):
            return binary_search(ordered_nums, index)
    return False
