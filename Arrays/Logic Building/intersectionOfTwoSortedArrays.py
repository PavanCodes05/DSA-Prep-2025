"""
Problem Statement: Given two sorted arrays, nums1 and nums2, return an 
array containing the intersection of these two arrays. Each element in the 
result must appear as many times as it appears in both arrays.

The intersection of two arrays is an array where all values are present in both arrays

TC:
1.  Input: nums1 = [1, 2, 2, 3, 5], nums2 = [1, 2, 7]
    Output: [1, 2]
    Explanation: The elements 1, 2 are the only elements present in both nums1 and nums2
2.  Input: nums1 = [1, 2, 2, 3], nums2 = [4, 5, 7]
    Output: []
    Explanation: No elements appear in both nums1 and nums2
"""

 
nums1 = [1, 2, 2, 3, 5]
nums2 = [1, 2, 7]

# Brute Force 
def intertsectionOfTwoSortedArraysBrute(nums1, nums2):
    # Create a resulting vector
    res = []
    # This array check if a elem in the nums2 arr is used or not
    visited = [0] * len(nums2)

    i = j = 0
    # We start in the first element of first array
    while i < len(nums1):
        # We traverse through the second array inner loop
        while j < len(nums2):
            # We check if both are equal and that elem in the second arr is unvisited
            if nums1[i] == nums2[j] and visited[j] == 0:
                # We add that element to the res arr and update it as visited
                res.append(nums2[j])
                visited[j] = 1
                break
            # If I see a greater elem there is no point looking beside it, Since it is sorted
            elif nums2[j] > nums1[i]:
                break
            j += 1
        i += 1

    return res

# Optimal
def intersectionOfTwoSortedArraysOptimal(nums1, nums2):
    res = []
    i = j = 0

    # We start at the first elem of both arrays
    while i < len(nums1) and j < len(nums2):
        # Move the pointer if I see a smaller value
        if nums1[i] < nums2[j]:
            i += 1
        elif nums2[j] < nums1[i]:
            j += 1
        # If seen a equal value, we append and move both the pointers together
        else:
            res.append(nums1[i])
            i += 1
            j += 1

    return res

res = intersectionOfTwoSortedArraysOptimal(nums1, nums2)
print(res)

"""
Approach:
    Brute: This is one of the very few problems, where i felt coming up with 
    optimal solution as a easier option, but i couldn't come up with the brute force
    solution easily, I had to take a look at the solution tab to figure this out, We use
    a nested loop to traverse through both the elements, we do this till we find an equal value
    this would give us all the common elements but we cannot track the number of occurances in
    both the arrays, that is why we use a visted[] of size nums2 which keeps track of the elements
    already visited and yet to be visited, and if i see a equal value and that is not visited yet
    then i add them to the resulting arr and I mark that as visited, and so on to find the values
    which is common as well as I can keep track of the number of occurances.

    Time: O(m * n)
    Space: O(n)

    Optimal: This optimal solution is very simple, we have two pointers each on start
    of each array, we compare values move the pointer of smaller value to get to the
    equal one, once we have equal values, add them to the resulting vector and 
    move both pointers at once, no problem of thinking the pointer getting out of bounds
    because the loop stops when either of the pointer goes out of bounds.

    Time: O(m) -> The smaller array exhausts if nothing matches, loop ends
    Space: O(1)
"""