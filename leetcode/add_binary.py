"""
Given two binary strings a and b, return their sum as a binary string.

 

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
 

Constraints:

1 <= a.length, b.length <= 104
a and b consist only of '0' or '1' characters.
Each string does not contain leading zeros except for the zero itself.

"""
class Solution:
    # This solution uses built-in functions 
     def addBinary(self, a: str, b: str) -> str:
        bin_a = int(a, 2)
        bin_b = int(b, 2)
        sum_of_binaries = bin_a + bin_b
        return str(bin(sum_of_binaries)[2:])
    
    # This solution uses a bit by bit calculation, not efficient
    def addBinary(self, a: str, b: str) -> str:
        max = len(a)
        if len(b) > len(a):
            max = len(b)
        c = ""
        carry = 0
        i = -1
        while abs(i) <= max:
            if abs(i) > len(a):
                d = carry + int(b[i])
            elif abs(i) > len(b):
                d = carry + int(a[i])
            else:
                d = carry + int(a[i]) + int(b[i])
            if d >= 2:
                carry = 1
                d = d - 2
            else:
                carry = 0
            c = str(d) + c
            print(str(d)+str(carry))
            i -= 1
            
        if carry:
            c = "1" + c
        return c
            