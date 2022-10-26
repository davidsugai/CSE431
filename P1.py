from random import randint
import matplotlib.pyplot as plt
import timeit

# Implementation of MergeSort
# https://www.geeksforgeeks.org/merge-sort/
def mergeSort(arr):
    if len(arr) > 1:
        # Finding the mid of the array
        mid = len(arr) // 2
        # Dividing the array elements
        L = arr[:mid]
        # into 2 halves
        R = arr[mid:]
        # Sorting the first half
        mergeSort(L)
        # Sorting the second half
        mergeSort(R)
        i = j = k = 0
        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1


# Implementation of insertion sort
# https://www.geeksforgeeks.org/python-program-for-insertion-sort/
def insertionSort(arr):
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
        key = arr[i]
        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


# Merge sort has an expected run time of Θ(nlogn); insertion sort has an expected run time of Θ(n^2).
# Insertion sort, however, turns out to be faster for very small n.
# Figure out how small.
if __name__ == '__main__':
    mergeArr, insertionArr = [], []
    mergeTimes, insertionTimes = [], []
    x = []

    for i in range(0, 100):
        rand = randint(1, 100)
        x.append(i + 1)
        mergeArr.append(rand)
        insertionArr.append(rand)
        mergeTemp = mergeArr.copy()
        insertionTemp = insertionArr.copy()
        mergeTimes.append(timeit.timeit("mergeSort(mergeTemp)", "from __main__ import mergeSort, mergeTemp", number=1))
        insertionTimes.append(timeit.timeit("insertionSort(insertionTemp)", "from __main__ import insertionSort, insertionTemp", number=1))

    plt.plot(x, mergeTimes, label="Merge")
    plt.plot(x, insertionTimes, label="Insertion")
    plt.xlabel('Array Length', fontsize=10)
    plt.ylabel('Time (s)', fontsize=10)
    plt.legend()
    plt.show()