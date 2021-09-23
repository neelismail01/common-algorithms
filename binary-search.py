def binary_search(input_array, value):
    left = 0
    right = len(input_array) - 1
    while left <= right:
        middle = (left + right) // 2
        if input_array[middle] == value:
            return middle
        elif input_array[middle] < value:
            left = middle + 1
        else:
            right = middle - 1
    return -1