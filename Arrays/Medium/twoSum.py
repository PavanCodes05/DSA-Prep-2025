"""
Problem Statement:
    Given an array of integers nums and an integer target. Return the indices(
    0 - indexed) of two elements in nums such that they add up to target.
    
    Each input will have exactly one solution, and the same element cannot be 
    used twice. Return the answer in non-decreasing order.

    TC:
1.  Input: nums = [1, 6, 2, 10, 3], target = 7
    Output: [0, 1]
    Explanation: nums[0] + nums[1] = 1 + 6 = 7

2.  Input: nums = [1, 3, 5, -7, 6, -3], target = 0
    Output: [1, 5]
    Explanation: nums[1] + nums[5] = 3 + (-3) = 0

3.  Input: nums = [-6, 7, 1, -7, 6, 2], target = 3
    Output:[2, 5]
"""

def twoSumBrute(nums, target):
    n = len(nums)

    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return [i, j]

def twoSumOptimal(nums, target):
    n = len(nums)
    
    val_dict = dict()
    for i in range(n):
        complement = target - nums[i]

        if complement in val_dict:
            return [val_dict[complement], i]
        else:
            val_dict[nums[i]] = i

nums = [1, 3, 5, -7, 6, -3]
target = 0

resBrute = twoSumBrute(nums, target)
print(resBrute)

resOptimal = twoSumOptimal(nums, target)
print(resOptimal)

"""
Approach:
    Brute: This is one of the early problems I solved in my early dsa days,
    and this is super intresting for it's difficulty, and Brute force solution for 
    this is quite straightforward, we just take a number and check it with everyother 
    number after it and sum it up and check if they are equal to the target that we are
    looking for, if yes we return the pair as array
        1. We are not checking the numbers before a number, because we are doing addition (2 + 1 = 1 + 2)
        2. We are not returning anything if no pair is found, that is because, we are guaranteed 
        atleast one solution, so we do not need to handle that case.

        Time: O(n **2)
        Space: O(1)

    Optimal: Here comes the interesting part of the problem, the optimal solution to this problem
    is so interesting, we maintain a hashmap, which keeps track of { val: idx } pair, and I iterate
    through every number and calculate a complement value (target - curVal) which gives us a number
    which can be added to the current number which can give us the target, if that value exists in our
    hashmap we can just return that value's index and the current value's index. We have to do this in
    a single loop, we cannot first do the hashmap and then run through each number, this could go wrong 
    if we have two same numbers in different indexes, this could mess up things, so we have to do it in 
    a single loop.

        Time: O(n)
        Space: O(1)
"""
