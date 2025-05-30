"""
Sort an array of 0's 1's and 2's

Problem Statement:
    Given an array nums consisting of only 0, 1, or 2. Sort the array 
    in non-decreasing order. The sorting must be done in-place, without 
    making a copy of the original array.

1.  Input: nums = [1, 0, 2, 1, 0]
    Output: [0, 0, 1, 1, 2]
    Explanation: The nums array in sorted order has 2 zeroes, 2 ones and 1 two

2.  Input: nums = [0, 0, 1, 1, 1]
    Output: [0, 0, 1, 1, 1]
    Explanation: The nums array in sorted order has 2 zeroes, 3 ones and zero twos

3.  Input: nums = [1, 1, 2, 2, 1]
    Output: [1, 1, 1, 2, 2]
"""

def sortOptimal(nums):
    n = len(nums)

    low, mid, high = 0, 0, n - 1

    while mid < high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1

nums = [1, 0, 2, 1, 0]
sortOptimal(nums)

print(nums)

"""
Approach:
    Brute and Better: I am not going to write up the brute and better solution for 
    this problem, because I dont think this is really neccessary because the solutions
    are pretty simple.
        Brute: nums.sort() => Time: O(n log n or n ** 2) Space: O(1)
        Better: coutn number of 0's, 1's, 2's and Modify them to the nums arr 
            Time -> O(2N) Space: O(1)
    
    Optimal: One of the simple yet interesting problem, The better solution even gives
    O(n) solution but still there is a much interesting way to solve this problem, That is 
    using `Dutch National Flag Algorithm`- This intersted me a lot.

    We have a big array such as [0, 0, 0, 0, 1, 1, 1, 1, 2, 1, 0, 1, 2, 2, 2, 2]
    We see a pattern in this => 
        1. 0 to low - 1 is 0's
        2. low to mid - 1 is 1's
        3. mid to high - 1 is 2's
        4. high to n - 1 is 2's
    
    We can start sorting the unsorted part by accessing the value pointed by mid pointer.
    If mid has value:
        0 -> We swap with low pointer and move low, mid pointer => + 1
        1 -> We do not do any swaps but move mid + 1
        2 -> We swap mid value with high and move high - 1

    By doing this the array becomes sorted.
    (Keep low and mid on 0 and high on n - 1) => for the given array.

    THIS IS JUST A INTERESTING WAY TO SOLVE THIS
        
        Time: O(n)
        Space: O(1)
"""