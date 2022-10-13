# Given an integer x, return true if x is palindrome integer.
# An integer is a palindrome when it reads the same backward as forward.
# For example, 121 is a palindrome while 123 is not.
class Solution:
    def isPalindrome(self, x: int) -> bool:
        number_to_string = str(x)
        n = len(number_to_string)
        
        for k in range(0, n//2):
            if number_to_string[k] != number_to_string[n-k-1]:
                return False
        return True