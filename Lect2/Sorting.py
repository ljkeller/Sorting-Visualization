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

if __name__ == '__main__':
    arr = [3, 11, 15, 2, 12, 9]
    arr2 = [3, 5, 9, 12, 20, 46]
    print("The array contents are: %s", arr)

    quick_sort(arr, 0, len(arr) - 1)
    print("The array contents are: %s", arr)


    insertion_sort(arr)