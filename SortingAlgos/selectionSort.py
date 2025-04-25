nums =  [7, 4, 1, 5, 3]

def selectionSort(nums):
    n = len(nums)

    # Outer loop runs from 0 -> n - 1(excluded)
    for i in range(n - 1):
        # Assume Current Value Is the Minimum
        min_pos = i
        # Inner Loop Runs from i -> n(excluded)
        for j in range(i, n):
            # Finds minimum (if exists)
            if nums[j] < nums[min_pos]:
                min_pos = j
        
        # Swap only if the min is found (Optimized Approach)
        if min_pos != i:
            nums[i], nums[min_pos] = nums[min_pos], nums[i]

selectionSort(nums)
print(nums)