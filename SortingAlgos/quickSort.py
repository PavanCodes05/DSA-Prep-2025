import random

nums = [7, 1, 4, 6, 0, 12, 21, 2]

def partition(arr, low, high):
    # Choose a random index to avoid messing up quick sort, because already sorted arrry could take up to O(n**2) time if not handled this way

    # generate random integer in arr range
    randomIndex = low + random.randint(0, high - low)
    # Swappin the random element with the first element just to ease the process 
    arr[low], arr[randomIndex] = arr[randomIndex], arr[low]

    # Setting the first element as pivot 
    pivot = arr[low]

    # Starting index for left and right subarray 
    i = low
    j = high 

    while i < j:
        # Move "i" to the right till we find a greater value than the pivot value
        while arr[i] <= pivot and i <= high - 1:
            i += 1

        # Move "j" to the left till we find a lesser value than the pivot
        while arr[j] > pivot and j >= low + 1:
            j -= 1
        
        # Swap element at i and j if i is still less than j
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[low], arr[j] = arr[j], arr[low]
    return j

def quickSortHelper(arr, low, high):
    # Base Case: if hte array has one or no elements which means the array is sorted
    if low < high:
        pIndex = partition(arr, low, high)

        quickSortHelper(arr, low, pIndex)
        quickSortHelper(arr, pIndex + 1, high)

def quickSort(nums):
    n = len(nums)

    quickSortHelper(nums, 0, n - 1)

    return nums

quickSort(nums)
print(nums)