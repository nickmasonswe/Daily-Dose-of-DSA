'''
2461. Maximum Sum of Distinct Subarrays With Length K
Medium
Topics
Companies
Hint

You are given an integer array nums and an integer k. Find the maximum subarray sum of all the subarrays of nums that meet the following conditions:

    The length of the subarray is k, and
    All the elements of the subarray are distinct.

Return the maximum subarray sum of all the subarrays that meet the conditions. If no subarray meets the conditions, return 0.

A subarray is a contiguous non-empty sequence of elements within an array.

 

Example 1:

Input: nums = [1,5,4,2,9,9,9], k = 3
Output: 15
Explanation: The subarrays of nums with length 3 are:
- [1,5,4] which meets the requirements and has a sum of 10.
- [5,4,2] which meets the requirements and has a sum of 11.
- [4,2,9] which meets the requirements and has a sum of 15.
- [2,9,9] which does not meet the requirements because the element 9 is repeated.
- [9,9,9] which does not meet the requirements because the element 9 is repeated.
We return 15 because it is the maximum subarray sum of all the subarrays that meet the conditions

Example 2:

Input: nums = [4,4,4], k = 3
Output: 0
Explanation: The subarrays of nums with length 3 are:
- [4,4,4] which does not meet the requirements because the element 4 is repeated.
We return 0 because no subarrays meet the conditions.

 

Constraints:

    1 <= k <= nums.length <= 105
    1 <= nums[i] <= 105

'''

class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        #init an empty set
        window_set = set()

        #init variables to track important data
        max_sum = 0
        current_sum = 0
        left_edge = 0
        # init right edge in loop

        #base case 
        if len(nums) < k:
            return 0

        #loop through length of nums, right_edge explores next elements
        for right_edge in range(len(nums)):
            #while the right_edge value is in the set, move the whole window up 
            if nums[right_edge] in window_set:
                window_set.remove(nums[left_edge])
                #decrease current_sum by nums[left_edge]
                #since we removed the left_edge while preparing to move it up
                current_sum -= nums[left_edge]
                #move the left_edge up
                left_edge += 1
                #the right_edge value is effectively the same, no change needed

            #for every loop that does not hit the while condition:
            #add the right_edge to the set
            window_set.add(nums[right_edge])
            #increase current_sum, 
            current_sum+= nums[right_edge]

            #grow window to correct size, k, accounting for off-by-one errors
            #if the window is the correct size, to move forward, we now need to
            #increment the left edge as we go, to match the above
            if right_edge - left_edge + 1 == k: #if k is 3, index 0 and index 2 are size 3. +1 needed.
                max_sum = max(current_sum,max_sum)
                #move the left Edgeup for the next round again, as above
                #the window is temporarily made smaller, and then restored
                #update the new, lower sum
                window_set.remove(nums[left_edge])
                current_sum -= nums[left_edge]
                left_edge += 1
        return max_sum
        
