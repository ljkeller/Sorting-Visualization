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

if __name__ == '__main__':
    arr = [3, 11, 15, 2, 12, 9]
    arr2 = [3, 5, 9, 12, 20, 46]
    print("The array contents are: %s", arr)

    insertion_sort(arr)
    print("The array contents are: %s", arr)


    insertion_sort(arr)