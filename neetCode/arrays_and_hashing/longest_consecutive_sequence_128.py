"""
128. Longest Consecutive Sequence
Solved
Medium
Topics
Companies

Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

 

Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9

 

Constraints:

    0 <= nums.length <= 105
"""
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest_seq = 0
        hash_set = set(nums)

        # loop through set once
        for el in hash_set:
        # find beginning of seq by finding el with no element that is one less than itself
            if el - 1 not in hash_set:
                current_seq_length = 0
            #while there is an el that fulfills the requirment keep increasing
            #check if el + 1,2,3 etc exist by using the current length of the sequence to add to el, ie if 3 +1, 3 + 2 etc exist
                while el + current_seq_length in hash_set:
                    current_seq_length += 1
                    longest_seq = max(longest_seq, current_seq_length)
        return longest_seq
