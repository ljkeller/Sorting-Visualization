import heapq
import math
import random


def bubble_sort(arr):
    swap = True
    count = 0
    for i in range(len(arr) - 1):  # only to n-2 because inner loop will
        # cause last element to be largest after first pass
        swap = False;
        for j in range(
                len(arr) - i - 1):  # Wont check already updated elements
            count += 1
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
                swap = True
        if not swap:
            print(count)
            return

    print(count)
    return


def insertion_sort(arr: list):
    for j in range(1, len(arr)):
        insert = arr[j]
        i = j - 1
        while i >= 0 and insert < arr[i]:  # stable, right to left
            arr[i + 1] = arr[i]
            i -= 1
        arr[i + 1] = insert


def quick_sort(arr, left, right):
    if left >= right:
        return

    p = partition(arr, left, right)
    quick_sort(arr, left, p - 1)
    quick_sort(arr, p + 1, right)


def heap_sort(arr):
    n = len(arr)
    heapify(arr)
    for i in range(len(arr)-1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        sift_down(arr, 0, i)

def heapify(arr: list) -> None:  # In place, linear time max-heap function
    """
    A linear time, in place function for creating a max-heap
    :param arr: Array to be turned into a max-heap
    """
    for i in range(len(arr) - 1, -1, -1):
        sift_down(arr, i, len(arr))


def sift_down(arr: list, node: int, n) -> None:
    """
    A log(h) time function to be used on an array node to heapify a subtree.
    Works bottom-up, as in parents smaller than children will swap,
    and iteratively continues.
    :param arr: Array to be sifted through
    :param node: Current parent node index of interest
    :param n: Size of array/tree
    """

    index = node
    if index >= n or index*2 + 1 >= n :
        return

    has_left_child = True
    left_child = arr[index * 2 + 1]
    has_right_child = True if index * 2 + 2 < n else False
    if has_right_child:
        right_child = arr[index * 2 + 2]
    else:
        right_child = None

    while has_left_child and arr[index] < arr[index * 2 + 1] or (
            has_right_child and arr[index] < arr[index * 2 + 2]):
        if has_left_child and has_right_child:
            max_child_index = 2 * index + 1 if left_child >= right_child \
                else 2 * index + 2
        else:
            max_child_index = 2 * index + 1
        arr[max_child_index], arr[index] = arr[index], arr[max_child_index]
        index = max_child_index

        if index*2 + 1 >= n:
            return
        else:
            left_child = arr[index*2 + 1]
            has_right_child = True if index * 2 + 2 < n else False
            if has_right_child:
                right_child = arr[index * 2 + 2]

def partition(arr, left, right):
    pivot = arr[left]
    i, j = left + 1, right
    while True:  # consider even or odd length lists
        while i <= j and arr[i] <= pivot:
            i += 1
        while i <= j and arr[j] >= pivot:
            j -= 1
        if i <= j:
            arr[j], arr[i] = arr[i], arr[j]
        else:
            break
    arr[left], arr[j] = arr[j], arr[left]  # swap pivot in
    return j


def digit_ordering(arr, max):
    num_digits = math.ceil(math.log(max, 10))
    digits_organized = [[] for i in range(10)]
    for i in range(num_digits):
        for j in range(len(arr)):
            digit = int((arr[j] // math.pow(10, i))) % 10
            digits_organized[digit].append(arr[j])
        arr[:] = [leaves for tree in digits_organized for leaves in tree]
        for sublist in digits_organized:
            sublist.clear()
    test = [elem for sublist in digits_organized for elem in sublist]
    return digits_organized


if __name__ == '__main__':
    arr = [3, 11, 15, 2, 12, 9]
    arr2 = [3, 5, 9, 12, 20, 46]
    rand_arr = [random.randint(0, 820) for i in range(175)]
    rand_arr2 = [random.randint(0, 820) for i in range(175)]

    heap_sort(arr)
    print(arr)

    heap_sort(rand_arr)
    print(rand_arr)
    # # print("The array contents are: %s", arr)
    #
    # x = digit_ordering(rand_arr, 820)
    # # print(x)
    #
    # quick_sort(arr, 0, len(arr) - 1)
    # # print("The array contents are: %s", arr)
    # print(rand_arr2)
    # heapq._heapify_max(rand_arr2)
    # print(rand_arr2.pop())
    # print(rand_arr2)
    # heap_sort(rand_arr2)
    # print("Also, the array: ", rand_arr2)
    #
    # insertion_sort(arr)
