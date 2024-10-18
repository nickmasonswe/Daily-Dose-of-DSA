"""
1. Two Sum
Solved
Easy
Topics
Companies
Hint

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]

"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        cur_sum = 0
        seen = {}
        for i in range(len(nums)):
            compl = target - nums[i]
            if compl in seen:
                return [i, seen[compl]]
            #add to seen last so that false positives from a num that is half of target is not found and used
            seen[nums[i]] = i

