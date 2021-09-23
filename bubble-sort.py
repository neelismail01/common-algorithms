def bubbleSort(array):
    # Write your code here.
	isSorted = False
	end = len(array) - 1
	
	while not isSorted:
		isSorted = True
		for i in range(end):
			if array[i] > array[i + 1]:
				array[i], array[i + 1] = array[i + 1], array[i]
				isSorted = False
		end -= 1
	return array