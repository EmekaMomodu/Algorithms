"""

  Write a function that takes in an array of integers and returns a sorted
  version of that array. Use the Bubble Sort algorithm to sort the array.

"""


def bubbleSort(array):
    sortedFlag = 0
    counter = 0
    while not sortedFlag:
        sortedFlag = 1
        for i in range(len(array) - 1 - counter):
            if array[i] > array[i + 1]:
                swap(array, i, i + 1)
                sortedFlag = 0
        counter += 1
    return array


def swap(array, i, j):
    array[i], array[j] = array[j], array[i]


