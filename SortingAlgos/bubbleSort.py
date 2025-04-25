nums = [13, 46, 52, 24]

def bubbleSort(nums):
    n = len(nums)
    # Range of outer loops have reduce for every pass
    for i in range(n - 1, -1, -1):
        # Keep track of the values being swapped
        isSwapped = False
        # Inner loops run from 0 to i(excluded)
        for j in range(i):
            # Swaps if not sorted
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                isSwapped = True
        # If after a pass nothing is swapped, which probably means the array is already sorted
        if not isSwapped:
            break

bubbleSort(nums)
print(nums)