"""
Problem Statement: Given two sorted arrays nums1 and nums2, return an 
array that contains the union of these two arrays. The elements in the 
union must be in ascending order.

The union of two arrays is an array where all values are distinct and are
present in either the first array, the second array, or both.

TC:
1.  Input: nums1 = [1, 2, 3, 4, 5], nums2 = [1, 2, 7]
    Output: [1, 2, 3, 4, 5, 7]
    Explanation: The elements 1, 2 are common to both, 3, 4, 5 are 
    from nums1 and 7 is from nums2

2.  Input: nums1 = [3, 4, 6, 7, 9, 9], nums2 = [1, 5, 7, 8, 8]
    Output: [1, 3, 4, 5, 6, 7, 8, 9]
    Explanation: The element 7 is common to both, 3, 4, 6, 9 are from nums1 and 1, 5, 8 is from nums2
"""

# Brute Force

nums1 = [1, 2, 3, 4, 5]
nums2 = [1, 2, 7]

def unionOfTwoSortedArraysBrute(nums1, nums2):
    # Create a set and store only unique elements of both
    s = set()
    # Empty array to store the resulting vector
    union = []

    # Traverse through the first arr and store only unique elements 
    for num in nums1:
        s.add(num)

    # Traverse through the second arr and store only unique elements 
    for num in nums2:
        s.add(num)

    # Finally traverse through the sorted set and add those elements to union arr
    for num in sorted(s):
        union.append(num)
    
    # Return the resulting array of sorted unique elements from nums1 and nums2
    return union

def unionOfTwoSortedArraysOptimal(nums1, nums2):
    # Empty array to store the result
    union = []

    # We initialize two pointers: One on first ele of nums1, another on first ele on nums2 
    i = j = 0
    m, n = len(nums1), len(nums2)

    # The loop runs till one of the array is traversed completely
    while i < m and j < n:
        # We compare and if we find the i-th value of nums1 is less than or equal to j-th of nums2
        if nums1[i] <= nums2[j]:
            # We would have to make sure that either union is empty or the last element is not 
            # being same as current
            if not union or union[-1] != nums1[i]:
                union.append(nums1[i])
            # We move the pointer anyways
            # Either new value is added or already exists(so we just move it)
            i += 1
        else:
            # Same for the other case where nums2[j] could be greater than nums1[i]
            if not union or union[-1] != nums2[j]:
                union.append(nums2[j])
            j += 1
    
    # After either of the arrays are traversed, we have to add the remaining 
    # elements to the resulting array.
    while i < m:
        if not union or union[-1] != nums1[i]:
            union.append(nums1[i])
        i += 1
    
    while j < n:
        if not union or union[-1] != nums2[j]:
            union.append(nums2[j])
        j += 1
    
    # Finally we return the resulting array
    return union

union = unionOfTwoSortedArraysOptimal(nums1, nums2)
print(union)


"""
Approach:
    Brute: Coming up with this brute force solution was quite easier than I thought,
    But the thing is even the brute force solution code for this is good & clean, 
    We have to find a way to merge both arrays and just have unique elements in sorted
    manner and return that, so we create a set and store unique elements from first and 
    second array right after each other, Now we would have a set of unique elements from both
    arrays but the order of the elements are not sorted, so we have to sort the set and add 
    the elements to the union arr, Since we are supposed to return an array.

    Time: O((m + n) ** 2) or O((m + n) * log(m + n)) -> Depends on the sorting algo we use
    Space: O(m + n) -> If both arrays have no common elements, we would have to use all elements 
    from both arrays.
    
    Brute to Optimal: We know that we have to return a new array, so we cannot optimize space, But 
    we can for sure do better with the time, we have to use the sorted property properly.

    Optimal: This approach is so good, this actually makes a lot of sense, we simulataneously
    check values from both the arrays, and add the lesser one, if we find a equal one, we just
    add any one of it, and we are making sure that it doesn't already exists in the resulting array
    This approach utilizes the sorted behaviour very well and reduces the time from O((m + n) * log(m + n))
    to O({m + n})

    Time: O((m + n))
    Space: O((m + n))
"""