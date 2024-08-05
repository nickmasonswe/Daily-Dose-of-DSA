class Solution:
    def isAnagram(self, s:str, t:str)-> bool:
        if len(s) != len(t):
            return False
        s_freq, t_freq = {} , {}
        for i in range(len(s)):
            s_letter = s[i]
            t_letter = t[i]
            s_freq[s_letter] = 1 + s_freq.get(s_letter, 0)
            t_freq[t_letter] = 1 + t_freq.get(t_letter, 0)
        return s_freq == t_freq

#see ts version for other approaches
'''
Given two strings s and t, return true if t is an anagram of s, and false otherwise.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
Example 1:
Input: s = "anagram", t = "nagaram"
Output: true
Example 2:
Input: s = "rat", t = "car"
Output: false
Constraints:
    1 <= s.length, t.length <= 5 * 104
    s and t consist of lowercase English letters.
'''
