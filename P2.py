from random import randint
import matplotlib.pyplot as plt
import timeit

# https://www.geeksforgeeks.org/timsort/
# Python3 program to perform basic timSort
MIN_MERGE = 16


def calcMinRun(n):
    """Returns the minimum length of a
    run from 23 - 64 so that
    the len(array)/minrun is less than or
    equal to a power of 2.

    e.g. 1=>1, ..., 63=>63, 64=>32, 65=>33,
    ..., 127=>64, 128=>32, ...
    """
    r = 0
    while n >= MIN_MERGE:
        r |= n & 1
        n >>= 1
    return n + r


# This function sorts array from left index to
# right index which is of size at most RUN
def insertion(arr, left, right):
    for i in range(left + 1, right + 1):
        j = i
        while j > left and arr[j] < arr[j - 1]:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j -= 1


# Merge function merges the sorted runs
def merge(arr, l, m, r):
    # original array is broken in two parts
    # left and right array
    len1, len2 = m - l + 1, r - m
    left, right = [], []
    for i in range(0, len1):
        left.append(arr[l + i])
    for i in range(0, len2):
        right.append(arr[m + 1 + i])

    i, j, k = 0, 0, l

    # after comparing, we merge those two array
    # in larger sub array
    while i < len1 and j < len2:
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1

        else:
            arr[k] = right[j]
            j += 1

        k += 1

    # Copy remaining elements of left, if any
    while i < len1:
        arr[k] = left[i]
        k += 1
        i += 1

    # Copy remaining element of right, if any
    while j < len2:
        arr[k] = right[j]
        k += 1
        j += 1


# Iterative Timsort function to sort the
# array[0...n-1] (similar to merge sort)
def hybridSort(arr):
    n = len(arr)
    minRun = calcMinRun(n)

    # Sort individual subarrays of size RUN
    for start in range(0, n, minRun):
        end = min(start + minRun - 1, n - 1)
        insertion(arr, start, end)

    # Start merging from size RUN (or 32). It will merge
    # to form size 64, then 128, 256 and so on ....
    size = minRun
    while size < n:

        # Pick starting point of left sub array. We
        # are going to merge arr[left..left+size-1]
        # and arr[left+size, left+2*size-1]
        # After every merge, we increase left by 2*size
        for left in range(0, n, 2 * size):

            # Find ending point of left sub array
            # mid+1 is starting point of right sub array
            mid = min(n - 1, left + size - 1)
            right = min((left + 2 * size - 1), (n - 1))

            # Merge sub array arr[left.....mid] &
            # arr[mid+1....right]
            if mid < right:
                merge(arr, left, mid, right)

        size = 2 * size


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



if __name__ == '__main__':
    mergeArr, insertionArr, hybridArr = [], [], []
    mergeTimes, insertionTimes, hybridTimes = [], [], []
    # hybridArr1, hybridArr2, hybridArr3 = [], [], []
    # hybridTimes1, hybridTimes2, hybridTimes3 = [], [], []
    x = []

    for i in range(0, 200):
        rand = randint(1, 200)
        x.append(i + 1)

        mergeArr.append(rand)
        insertionArr.append(rand)
        hybridArr.append(rand)
        # hybridArr1.append(rand)
        # hybridArr2.append(rand)
        # hybridArr3.append(rand)

        mergeTemp = mergeArr.copy()
        insertionTemp = insertionArr.copy()
        hybridTemp = hybridArr.copy()
        # hybridTemp1 = hybridArr1.copy()
        # hybridTemp2 = hybridArr2.copy()
        # hybridTemp3 = hybridArr3.copy()

        mergeTimes.append(timeit.timeit("mergeSort(mergeTemp)", "from __main__ import mergeSort, mergeTemp", number=1))
        insertionTimes.append(timeit.timeit("insertionSort(insertionTemp)", "from __main__ import insertionSort, insertionTemp", number=1))
        hybridTimes.append(timeit.timeit("hybridSort(hybridTemp)", "from __main__ import hybridSort, hybridTemp", number=1))
        # MIN_MERGE = 8
        # hybridTimes1.append(timeit.timeit("hybridSort(hybridTemp1)", "from __main__ import hybridSort, hybridTemp1", number=1))
        # MIN_MERGE = 32
        # hybridTimes2.append(timeit.timeit("hybridSort(hybridTemp2)", "from __main__ import hybridSort, hybridTemp2", number=1))
        # MIN_MERGE = 64
        # hybridTimes3.append(timeit.timeit("hybridSort(hybridTemp3)", "from __main__ import hybridSort, hybridTemp3", number=1))
        # MIN_MERGE = 16

    plt.plot(x, mergeTimes, label="Merge")
    plt.plot(x, insertionTimes, label="Insertion")
    # plt.plot(x, hybridTimes1, label="Hybrid 8")
    plt.plot(x, hybridTimes, label="Hybrid 16")
    # plt.plot(x, hybridTimes2, label="Hybrid 32")
    # plt.plot(x, hybridTimes3, label="Hybrid 64")
    plt.xlabel('Array Length', fontsize=10)
    plt.ylabel('Time (s)', fontsize=10)
    plt.legend()
    plt.show()
