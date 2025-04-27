nums = [7, 2, 1, 3, 12, 5, 8]

"""
We need three different functions
1. One to divide the array into smaller pieces
2. One to merge the array into sorted ones
3. One to call both the functions in proper order to make mergesort possible
"""

def divide(arr, low, high):
    # Base case: Only one element is left or None
    if low >= high:
        return
    
    # Calculate mid value to divide the array
    mid = (low + high) // 2

    # Call the divide function on left, right subarrays
    divide(arr, low, mid)
    divide(arr, mid + 1, high)

    # Once the array is broken down, we need merge them in a sorted order
    merge(arr, low, mid, high)

def merge(arr, low, mid, high):
    # Temp array to store sorted values
    temp = []
    
    # Pointer on first element of the left subarray
    left = low
    # Pointer on first element of the right subarray
    right = mid + 1

    # Loop runs till either one of the pointers exceed the length of subarrays 
    while left <= mid and right <= high:
        if arr[left] < arr[right]:
            temp.append(arr[left])
            left += 1
        else:
            temp.append(arr[right])
            right += 1
    
    # Leftover elements to be added if any
    while left <= mid:
        temp.append(arr[left])
        left += 1
    
    while right <= high:
        temp.append(arr[right])
        right += 1
    
    # Replace/modify the elements to the original array
    for i in range(low, high + 1):
        arr[i] = temp[i - low]

def mergeSort(arr):
    n = len(arr)

    low = 0
    high = n - 1
    
    divide(arr, low, high)

    return arr

mergeSort(nums)
print(nums)