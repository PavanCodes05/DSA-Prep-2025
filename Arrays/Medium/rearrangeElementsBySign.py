"""
Problem Statemnt: Given an integer array nums of even length consisting of an 
equal number of positive and negative integers.Return the answer array in such a
way that the given conditions are met:

* Every consecutive pair of integers have opposite signs.
* For all integers with the same sign, the order in which they were present in nums 
is preserved.
* The rearranged array begins with a positive integer.

TC:

Input : nums = [2, 4, 5, -1, -3, -4]
Output : [2, -1, 4, -3, 5, -4]
Explanation: The positive number 2, 4, 5 maintain their relative positions 
and -1, -3, -4 maintain their relative positions

Input : nums = [1, -1, -3, -4, 2, 3]
Output : [1, -1, 2, -3, 3, -4]
Explanation: The positive number 1, 2, 3 maintain their relative positions 
and -1, -3, -4 maintain their relative positions
"""

nums = [2, 4, 5, -1, -3, -4]

def rearrangeElementsBySignBrute(nums):
    # Store positive and negative elements seperately
    pos = []
    neg = []

    # Traverse through the array and split the pos & neg values (The order should not change)
    for num in nums:
        if num > 0:
            pos.append(num)
        else:
            neg.append(num)
    
    # Modify the nums array by changing values pos-neg-pos-neg...(in same order)
    # We are using the len(pos) since both the arrays are gonna be of same size
    for i in range(len(pos)):
        # 2 * i gives the even position
        nums[2 * i] =  pos[i]
        # 2 * i + 1 gives the odd position
        nums[2 * i + 1] = neg[i]
    
    return nums

def rearrangeElementsBySignOptimal(nums):
    # We create the resulting vector of same size as given nums full of zeros to replace later.
    ans = [0] * len(nums)

    # First positions to be filled with pos and neg numbers
    posIdx, negIdx = 0, 1

    # We traverse through the array
    for num in nums:
        # If we see a neg value, we add it to the curIdx of negIdx
        if num < 0:
            ans[negIdx] =  num
            # We have to update the pointer to the next place 1->3->5->7...
            negIdx += 2 
        else:
            # If we see a positive value, we add it to the curIdx of posIdx
            ans[posIdx] = num
            # We update the pointer to next place for positive numbers 0->2->4->6....
            posIdx += 2
        
    return ans

res = rearrangeElementsBySignOptimal(nums)
print(res)


"""
Approach:
    Brute: The brute force solution for this problem is quite easy to understand, 
    cause we just loop through the given array and store positive and negative integers
    seperately, then we modify the given array using the positve and negative integer array
    we modify by adding the positive element first and negative element second and so on...

    Time: O(n + n / 2) -> n / 2 Since we traverse only half of the size of entire array
    Space: O(1) -> we modify the given array, no new space

    Brute to Optimal: Even the brute-force solution looks good it could be rounded up to O(n)
    but we can still try to make it up perfect O(n).

    Optimal: We can create a res array of size n full of zeros, we can have one pointer pointing
    to the first position of positive integer and another pointer pointing the first place for the
    negative integer, and we traverse through the array, we see a pos value, we modify the current 
    positive pointer pos to the curVal and then move the pointer 2-places ahead, and we do the same
    when we see negative value for negIdx. finally we would have the desired array which meets
    all the conditions given.

    Time: O(n)
    Space: O(n)
"""