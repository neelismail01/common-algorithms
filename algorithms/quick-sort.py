def partition(arr, left, right):
    pivot = arr[(left + right) // 2]
    while left <= right:
        while arr[left] < pivot:
            left += 1
        while right >= left and arr[right] > pivot:
            right -= 1

        if left <= right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1

    return left

def quick_sort(arr, left, right):
    index = partition(arr, left, right)
    if left < index - 1:
        quick_sort(arr, left, index - 1)

    if index < right:
        quick_sort(arr, index, right)


def printArray(arr, n):
    for i in range(n):
        print(arr[i], end=' ')
    print()

if __name__ == '__main__':
    arr = [4, 10, 5, 3, 6, 7, 2, 9]
    quick_sort(arr, 0, len(arr) - 1)
    printArray(arr, len(arr))