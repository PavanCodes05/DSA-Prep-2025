"""
Problem Statement: Given an integer array nums sorted in non-decreasing order, 
remove all duplicates in-place so that each unique element appears only once. 
Return the number of unique elements in the array.


If the number of unique elements be k, then,

*   Change the array nums such that the first k elements of nums 
    contain the unique values in the order that they were present originally.

*   The remaining elements, as well as the size of the array does not matter in terms of
    correctness.

An array sorted in non-decreasing order is an array where every element to the 
right of an element is either equal to or greater in value than that element.

TC:
1.  Input: nums = [0, 0, 3, 3, 5, 6]
    Output: 4
    Explanation: Resulting array = [0, 3, 5, 6, _, _]
    There are 4 distinct elements in nums and the elements marked as _ can have any value.

2.  Input: nums = [-2, 2, 4, 4, 4, 4, 5, 5]
    Output: 4
    Explanation: Resulting array = [-2, 2, 4, 5, _, _, _, _]
    There are 4 distinct elements in nums and the elements marked as _ can have any value.
"""

# Brute Force Solution

nums = [0, 0, 3, 3, 5, 6]

def removeDuplicatesBrute(nums):
    # Keep track of added elements
    seen = set()
    # Temp array to store only unique elements
    temp = []

    # Traverse through the array to add unique elements to temp[] 
    for num in nums:
        if num not in seen:
            temp.append(num)
            seen.add(num)

    # Modify the first 'k' values of actual array
    for i in range(len(temp)):
        nums[i] = temp[i]

    # We have return the number of k elements
    return len(temp)

# Optimal Solution

def removeDuplicatesOptimal(nums):
    # If the array is empty, which means there no unique elements or duplicates
    if not nums:
        return 0
    # We know that the first element is perfect: Sorted, not a duplicate 
    i = 0

    # We look for the next element to be placed after i
    for j in range(1, len(nums)):
        # We find a non-equal element to i
        if nums[i] != nums[j]:
            # Place it right after i 
            i += 1
            nums[i] = nums[j]
    # Current pos of 'i' has the number of unique elements, since 'i' starts from 0 we add 1 and return
    return i + 1

count_unique = removeDuplicatesOptimal(nums)

print(nums)
print(count_unique)


"""
Approach:
    Brute Force: The brute force solution was very easy to come up with
    because of the previous problem we have solved before this, this is 
    very similar and we came up with this solution pretty quick, we just 
    have to create a new array and add just unique elements to it, we have 
    the set to make sure that we add only unique elements to the list, we 
    specifically used a set because the look up time to search a value in 
    a set is o(n), instead if we used a list to lookup it would have been o(n)
    in the loop it would have become o(n**2), so we used a set, finally we moved
    the unique elements to the actual array because the question demands to make 
    all this happen in-place, finally we return the length of the temp array which 
    has all the unique elemments.

    Time: O(n)
    Space: O(k) but k can be equal to n when all the elements are unique, so it could be O(n)

    We have to find a way to not to use extra space to store the result

    Optimal: The optimal solution is very similar to the last problem we solved,
    In last problem we had to move all the zeros to the end, now we have to move 
    all the duplicates to somewhere, we doesn't have to explicitly move it to the 
    end but it is possible, We use two pointers, 'i' being with the first element, 
    because we know that element is already perfect,if we have only one element that 
    is going to be perfect, so we keep the other pointer on the next element and we 
    move the right pointer till we find a non-equal value of the first pointer, once 
    we find that we move the 'i' pointer and assign the non-equal value to the current 
    'i' position, now we have the perfect values alligned in the same order but avoiding 
    duplicates, now we can finally return the 'i + 1' value, because the final value inserted 
    in the i-th position will be the number of unique elements and as i starts from 0 
    we have to add 1 to it and return it.

    Time: O(n)
    Space: O(1) -> Everything is done in-place
"""