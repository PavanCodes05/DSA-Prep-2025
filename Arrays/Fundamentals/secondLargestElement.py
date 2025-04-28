"""
Problem Statement: Given an array of integers nums, return the 
second-largest element in the array. If the second-largest 
element does not exist, return -1.

TC: 
1.  Input: nums = [8, 8, 7, 6, 5]
    Output: 7
    Explanation: The largest value in nums is 8, the second largest is 7

2.  Input: nums = [10, 10, 10, 10, 10]
    Output: -1
    Explanation: The only value in nums is 10, so there is 
    no second largest value, thus -1 is returned

3.  Input: nums = [7, 7, 2, 2, 10, 10, 10]
    Output:7
"""

nums = [8, 8, 7, 6, 5]

def secondLargestElement(nums):
    # Two variables to compare and update with larger values
    largestElement = float("-inf")
    secondLargestElement = float("-inf")

    # Traverse through the array to find & compare other values
    for num in nums:
        # Check if the value is higher than the existing largest value
        if num > largestElement:
            # If yes, we have to move the current largest to the secondLargest
            secondLargestElement = largestElement
            # And assign the current value to the largestElement
            largestElement = num

            # If not larger than largestElement, We can check with the secondLargest 
            # We also have to make sure that curVal is not equal to the largestElement
        elif num > secondLargestElement and num != largestElement:
            secondLargestElement = num

    # Check if the secondLargest is found 
    if secondLargestElement != float("-inf"):
        return secondLargestElement
    # If the number doesn't return in the previous if statemnt, which means the number is not found
    # So return -1 (secondLargestElement not found)
    return -1

res = secondLargestElement(nums)
print(f"The Second Largest Element In The Array nums: {res}")


"""
Approach: We have to keep track of the secondLargest element, and the approach
I have come up with is the optimal one, we can initially have the largestElement
and secondLargestElement values as "-inf" to make sure we can handle even the 
negative values in the array for comparing. As we have our placeholders init
we can start traversing, we compare each number with the largestELement first,
if it is greater than largestElement we move the existing largest to the secondLargest
and assign the currentVal to the largest, if the number is not greater than the largest
we can compare it with the secondLargest, the number should be both greater than secondLargest
and should not be equal to the largestElements to avoid duplicates. if both doesnt check we
dont do anything.

Time: O(n) -> Traversing the entire array and comparing values(O(1)).
Space: O(1) -> We are not using any extra space.
"""