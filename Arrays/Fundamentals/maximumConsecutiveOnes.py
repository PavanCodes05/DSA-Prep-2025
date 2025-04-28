"""
Problem Statement: Given a binary array nums, return the maximum number 
of consecutive 1s in the array.
A binary array is an array that contains only 0s and 1s.

TC:
1.  Input: nums = [1, 1, 0, 0, 1, 1, 1, 0]
    Output: 3
    Explanation: The maximum consecutive 1s are present from index 4 to index 6, amounting to 3 1s

2.  Input: nums = [0, 0, 0, 0, 0, 0, 0, 0]
    Output: 0
    Explanation: No 1s are present in nums, thus we return 0
"""

nums = [1, 1, 0, 0, 1, 1, 1, 0]

def maxConsecutiveOnes(nums):
    # We need two vars: o
    # One to store the maximum it we had so far
    maxConsecutive = 0
    # One to store the current maximum
    temp = 0

    # We traverse through the array   
    for num in nums:
        # If the number is 0, we reset the temp to "0" to mark the end of the prev sequence
        if num == 0:
            temp = 0
        # If the number is not zero, we add 1 to the marking the sequence still continues
        else:
            temp += 1
            # We update the maxConsecutive everytime we add the count to the current sequence
            # We cannot update the maxConsecutive only when we see a zero, because not every
            # array ends with a zero, so it is safer to update the max everytime we see a sequence
            maxConsecutive = max(temp, maxConsecutive)
    
    return maxConsecutive

res = maxConsecutiveOnes(nums)
print(res)


"""
Approach: The first approach this to was pretty lame, glad that I learnt something out of it, 
My first approach was to update the max var whenever i see a zero and then reset the temp
but it doesn't work that way, we cannot guarantee that eveytime the sequence ends with a zero
so i had to update the max everytime I add something to the sequence, this way we still have the
track of the maximum consecutive 1's we saw so far.

We have the max var to store the maximum consecutive we have ever seen
and the temp variable to count individual sequence, and resets when it sees a '0'
and updates whenever it sees a addition to its sequence 'ie seeing a 1'

Time: O(n) -> We just traverse the array once, and update some values in constant time.
Space: O(1) -> We are not using any extra 'n' space to store anything.
"""