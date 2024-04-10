'''
PROBLEM DESCRIPTION:

Sort a list of integers in ascending order.
'''

# solution 1 - merge sort
'''The idea is to use merge sort to sort the list.
    The base case is when the list is empty or has only one element,
    return the list.
    Otherwise, divide the list into two halves,
    recursively sort each half, and merge the two sorted halves.
'''


def merge_sort(lst):
    if len(lst) <= 1:
        return lst

    mid = len(lst) // 2
    left = merge_sort(lst[:mid])
    right = merge_sort(lst[mid:])

    return merge(left, right)


def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1

    return result


# solution 2 - quick sort
'''The idea is to use quick sort to sort the list.
    The base case is when the list is empty or has only one element,
    return the list.
    Otherwise, choose a pivot element,
    partition the list into two halves,
    recursively sort each half, and concatenate the two sorted halves.
'''


def quick_sort(lst):
    if len(lst) <= 1:
        return lst

    pivot = lst[len(lst) // 2]
    left = [x for x in lst if x < pivot]
    middle = [x for x in lst if x == pivot]
    right = [x for x in lst if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)


# solution 3 - bubble sort
'''The idea is to use bubble sort to sort the list.
    Iterate over the list and for each element,
    compare it with the next element,
    swap them if they are in the wrong order.
    Repeat this process until the list is sorted.
'''


def bubble_sort(lst):
    n = len(lst)
    for i in range(n):
        for j in range(0, n-i-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst


# solution 4 - selection sort
'''The idea is to use selection sort to sort the list.
    Iterate over the list and for each element,
    find the minimum element in the rest of the list,
    swap it with the current element.
    Repeat this process until the list is sorted.
'''


def selection_sort(lst):
    n = len(lst)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if lst[j] < lst[min_idx]:
                min_idx = j
        lst[i], lst[min_idx] = lst[min_idx], lst[i]
    return lst


# solution 5 - insertion sort
'''The idea is to use insertion sort to sort the list.
    Iterate over the list and for each element,
    insert it into the correct position in the sorted part of the list.
    Repeat this process until the list is sorted.
'''


def insertion_sort(lst):
    n = len(lst)
    for i in range(1, n):
        key = lst[i]
        j = i-1
        while j >= 0 and key < lst[j]:
            lst[j+1] = lst[j]
            j -= 1
        lst[j+1] = key
    return lst


# solution 6 - heap sort
'''The idea is to use heap sort to sort the list.
    Build a max heap from the list,
    repeatedly extract the maximum element from the heap,
    and rebuild the heap until the list is sorted.
'''


def heapify(lst, n, i):
    largest = i
    le = 2*i + 1
    r = 2*i + 2

    if le < n and lst[le] > lst[largest]:
        largest = le

    if r < n and lst[r] > lst[largest]:
        largest = r

    if largest != i:
        lst[i], lst[largest] = lst[largest], lst[i]
        heapify(lst, n, largest)


def heap_sort(lst):
    n = len(lst)

    for i in range(n//2 - 1, -1, -1):
        heapify(lst, n, i)

    for i in range(n-1, 0, -1):
        lst[i], lst[0] = lst[0], lst[i]
        heapify(lst, i, 0)

    return lst
