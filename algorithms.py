### quick sort
def partition(arr, start, end):
    pivot = arr[(start + end) // 2]
    i = start
    j = end
    while i < j:
        while arr[i] < pivot:
            i += 1
        while j >= i and arr[j] > pivot:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    return j

def quick_sort(arr, start, end):
    if start < end:
        pivot = partition(arr, start, end)
        quick_sort(arr, start, pivot)
        quick_sort(arr, pivot + 1, end)


def printArray(arr, n):
    for i in range(n):
        print(arr[i], end=' ')
    print()

if __name__ == '__main__':
    arr = [4, 10, 5, 3, 6, 7, 2, 9]
    quick_sort(arr, 0, len(arr) - 1)
    printArray(arr, len(arr))