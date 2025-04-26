nums = [7, 2, 1, 3, 12, 5, 8]

def merge(arr, low, mid, high):
    temp = []

    left = low
    right = mid + 1

    while left <= mid and right <= high:
        if arr[left] <= arr[right]:
            temp.append(arr[left])
            left += 1
        elif arr[right] <= arr[left]:
            temp.append(arr[right])
            right += 1
        
    if left <= mid:
        temp.extend(nums[left:])

    if right <= high:
        temp.extend(nums[right:])

    for i in range(low, high + 1):
        arr[i] = temp[i - low]

def divide(arr, low, high):
    if low >= high:
        return

    mid = (low + high) // 2
    divide(arr, low, mid)
    divide(arr, mid + 1, high)

    merge(arr, low, mid, high)

def mergeSort(arr):
    n = len(arr)
    divide(arr, 0, n - 1)

mergeSort(nums)

print(nums)