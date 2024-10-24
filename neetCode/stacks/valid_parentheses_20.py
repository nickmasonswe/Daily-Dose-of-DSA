"""
20. Valid Parentheses
Solved
Easy
Topics
Companies
Hint

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
    Every close bracket has a corresponding open bracket of the same type.

 

Example 1:

Input: s = "()"

Output: true

Example 2:

Input: s = "()[]{}"

Output: true

Example 3:

Input: s = "(]"

Output: false

Example 4:

Input: s = "([])"

Output: true

 

Constraints:

    1 <= s.length <= 104
    s consists of parentheses only '()[]{}'.


"""

class Solution:
    def isValid(self, s: str) -> bool:
        parenMap = {
            ')' : '(',
            ']' : '[',
            '}' : '{'
        }
        # opening = ['(', '[', '{']
        # closing = [')',']','}']
        parenStack = []
        for char in s:
            #if char is a closing paren/ key of parenMap
            if char in parenMap:
                if parenStack and parenStack[-1] == parenMap[char]:
                    parenStack.pop()
                else:
                     return False
            # else if the char is an opening paren append it to the stack
            else:
                parenStack.append(char)
        #if there is nothing left in the stack, return true, else if there is still something there that was not matched, return false
        if not parenStack:
            return True
        else:
            return False 
