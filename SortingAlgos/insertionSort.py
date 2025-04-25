nums = [5, 2, 4, 6, 1]

def insertionSort(nums):
    n = len(nums)

    for i in range(1, n):
       j = i
       while j > 0 and nums[j - 1] > nums[j]:
           nums[j - 1], nums[j] = nums[j], nums[j - 1]
           j -= 1

insertionSort(nums)
print(nums)