"""

Problem:
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
 

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.

"""

class Solution:
    def isValid(self, s: str) -> bool:
        char_stack = []
        open_close = {
            "(" : ")",
            "{" : "}",
            "[" : "]"
        }
            
        for c in s:
            
            if c == '(' or c == '[' or c == '{':
                char_stack.append(c)
            elif len(char_stack):
                last_c = char_stack.pop()
                if c != open_close[last_c]:
                    return False
            elif not len(char_stack):
                return False
        if (len(char_stack)):
            return False
        else:
            return True