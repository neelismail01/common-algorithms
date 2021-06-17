def quick_sort(arr):
    length = len(arr)
    if length <= 1:
        return arr
    
    pivot = arr.pop()
    items_greater = []
    items_lower = []
    items_equal = [pivot]

    for item in arr:
        if item > pivot:
            items_greater.append(item)
        elif item < pivot:
            items_lower.append(item)
        else:
            items_equal.append(item)
    
    len(items_equal)
    return quick_sort(items_lower) + items_equal + quick_sort(items_greater)

print(quick_sort([10, 5, 3, 6, 7, 2, 9]))