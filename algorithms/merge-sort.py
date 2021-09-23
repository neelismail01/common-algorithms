def mergeSort(array):
    if len(array) == 1:
        return array
    middleIdx = len(array) // 2
    leftHalf = array[:middleIdx]
    rightHalf = array[middleIdx:]
    return merge(mergeSort(leftHalf), mergeSort(rightHalf))

def merge(leftHalf, rightHalf):
	sortedArray = [None] * (len(leftHalf) + len(rightHalf))
	k = i = j = 0
	while i < len(leftHalf) and j < len(rightHalf):
		if leftHalf[i] <= rightHalf[j]:
			sortedArray[k] = leftHalf[i]
			i += 1
		else:
			sortedArray[k] = rightHalf[j]
			j += 1
		k += 1
	while i < len(leftHalf):
		sortedArray[k] = leftHalf[i]
		i += 1
		k += 1
	while j < len(rightHalf):
		sortedArray[k] = rightHalf[j]
		j += 1
		k += 1
	return sortedArray
