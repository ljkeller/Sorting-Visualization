import math
import random
import heapq

def bubble_sort(arr):
    swap = True
    count = 0
    for i in range(len(arr) - 1): # only to n-2 because inner loop will
        # cause last element to be largest after first pass
        swap = False;
        for j in range(len(arr) - i - 1): # Wont check already updated elements
            count += 1
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
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
        while i >= 0 and insert < arr[i]: #stable, right to left
            arr[i+1] = arr[i]
            i-=1
        arr[i+1] = insert

def quick_sort(arr, left, right):
    if left >= right:
        return

    p = partition(arr, left, right)
    quick_sort(arr, left, p-1)
    quick_sort(arr, p+1, right)

def heap_sort(arr):
    for i in range(len(arr)):
        arr[0], arr[len(arr) - 1 - i] = arr[len(arr) - 1 - i], arr[0]
        temp = arr[:len(arr) - 1 - i]
        heapq._heapify_max(temp)
        arr[:len(arr) - 1 - i] = temp


def partition(arr, left, right):
    pivot = arr[left]
    i, j = left + 1, right
    while True: # consider even or odd length lists
        while i <= j and arr[i] <= pivot:
            i += 1
        while i <= j and arr[j] >= pivot:
            j -= 1
        if i <= j:
            arr[j], arr[i] = arr[i], arr[j]
        else:
            break
    arr[left], arr[j] = arr[j], arr[left] # swap pivot in
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

    #print("The array contents are: %s", arr)

    x = digit_ordering(rand_arr, 820)
    #print(x)


    quick_sort(arr, 0, len(arr) - 1)
    #print("The array contents are: %s", arr)
    print(rand_arr2)
    heapq._heapify_max(rand_arr2)
    print(rand_arr2.pop())
    print(rand_arr2)
    heap_sort(rand_arr2)
    print("Also, the array: ", rand_arr2)

    insertion_sort(arr)
