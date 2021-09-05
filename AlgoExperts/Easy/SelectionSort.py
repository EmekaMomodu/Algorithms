def selectionSort(array):
    smallestIdx = 0
    arrayLength = len(array)
    j = 0
    while j < arrayLength:
        for i in range(j, len(array)):
            if array[i] < array[smallestIdx]:
                smallestIdx = i
        swap(j, smallestIdx, array)
        j += 1
        smallestIdx = j
    return array


def swap(i, j, array):
    array[i], array[j] = array[j], array[i]