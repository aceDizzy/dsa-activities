import sys

def insertion_sort(arr):
    # This function will sort the array in non-decreasing order.
    n = len(arr)
    # After each iteration first i+1 elements are in sorted order.
    for i in range(1,n):
        key = arr[i]
        j = i-1
        # In each iteration shift the elements of aa[0..i-1],
        # that are greater than key, to one position ahead
        # of their current position
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
            arr[j+1] = key
    return arr

# main code
if __name__=='__main__':

    arr = [24,17,66,33,72,47,68,41,105,30]
    print("Sorted array: ")
    print(insertion_sort(arr))