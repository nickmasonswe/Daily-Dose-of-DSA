"""
3. Longest Substring Without Repeating Characters
Solved
Medium
Topics
Companies
Hint

Given a string s, find the length of the longest
substring
without repeating characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # sliding window resets left edge to one more than where it started
        # right side continues to grow until it hits a letter that is already in the set.
        cur_set = set()
        max_window_size = 0
        left = 0

        for right in range(len(s)):
            while s[right] in cur_set:
                cur_set.remove(s[left])
                left += 1
                max_window_size = max(max_window_size, cur_window_size)
                

            cur_window_size = right - left + 1
            cur_set.add(s[right])
            max_window_size = max(max_window_size, cur_window_size)
        return max_window_size
