"""
Problem Statement:
    Given an integer array nums. Return all triplets such that:

    i != j, i != k, and j != k
    nums[i] + nums[j] + nums[k] == 0.


    Notice that the solution set must not contain duplicate triplets. 
    One element can be a part of multiple triplets. The output and the 
    triplets can be returned in any order.

1.  Input: nums = [2, -2, 0, 3, -3, 5]
    Output: [[-2, 0, 2], [-3, -2, 5], [-3, 0, 3]]
    Explanation: nums[1] + nums[2] + nums[0] = 0
                 nums[4] + nums[1] + nums[5] = 0
                 nums[4] + nums[2] + nums[3] = 0

2.  Input: nums = [2, -1, -1, 3, -1]
    Output: [[-1, -1, 2]]
    Explanation: nums[1] + nums[2] + nums[0] = 0
    Note that we have used two -1s as they are separate elements 
    with different indexes But we have not used the -1 at index 4 
    as that would create a duplicate triplet

3.  Input: nums = [8, -6, 5, 4]
    (Give answer with the output and triplets sorted in ascending order)
    Output: []
"""

def threeSumBrute(nums):
    n = len(nums)
    triplets = set()

    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if nums[i] + nums[j] + nums[k] == 0:
                    temp = [nums[i], nums[j], nums[k]]
                    temp.sort()

                    triplets.add(tuple(temp))
    
    return [list(triplet) for triplet in triplets]

def threeSumOptimal(nums):
    n = len(nums)
    nums.sort()

    res = []

    for i in range(n):

        if i > 0 and nums[i] == nums[i - 1]:
            continue

        j = i + 1
        k = n - 1

        while j < k:
            summ = nums[i] + nums[j] + nums[k]

            if summ < 0:
                j += 1
            elif summ > 0:
                k -= 1
            else:
                res.append([nums[i], nums[j], nums[k]])
                j += 1
                k -= 1

                while j < k and nums[j] == nums[j - 1]:
                    j += 1
                while j < k and nums[k] == nums[k + 1]:
                    k -= 1
    return res

nums = [2, -2, 0, 3, -3, 5]

resBrute = threeSumBrute(nums)
print(resBrute)

resOptimal = threeSumOptimal(nums)
print(resOptimal)

"""
Approach:
    Brute: This is some of the very interesting problem, one of the follow
    ups after doing two-sum, this problem has quite more constraints than other
    similar problems, So we need a good understanding for solving this problem
    even for the brute force.

    We can easily run triple loops to get the value, but as the question says
    the array contains duplicates and result array cannot contain any duplicate
    triplets.

    So we need a set that maintains the unique triplets, Whenever we get a triplet
    summing up to 0, we sort that and add to set as tuple(Since sets do not support lists)
    This way the triplets stored are unique.

    We can finally return the set of tuples as list of lists.

        Time: O(n**3)
        Space: O(2K)
    
    Optimal: Optimal solution for this is to use a better time complexity and also
    not to use any extra space than the output array, Solving the TwoSum-II has been 
    very useful to solve this problem.

    We can sort the array and keep loop for n, and two pointers one on next to cur element
    and one on last element, we add up and if it is greater than 0, we reduce the given number
    by moving the right pointer one place down, and if it is lesser we move the left pointer
    one place up to increase the sum, and if it correctly evaluates to 0 we add three values to the 
    res array as triplet

    We have to make sure about the duplicates, since we are not having a extra set to take care of 
    avoiding duplicates, we have to avoid duplicates, and sorted property helps us a lot, whenever
    we see a element that we have already used as part of triplet we skip it, if cur and prev element is
    same we skip it.

    Finally we return the result.

        Time: O(n ** 2)
        Space: O(1)
"""
