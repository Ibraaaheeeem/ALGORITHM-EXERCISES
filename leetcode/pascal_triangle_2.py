"""
THE PROBLEM 
Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

 

Example 1:

Input: rowIndex = 3
Output: [1,3,3,1]

Example 2:

Input: rowIndex = 0
Output: [1]

Example 3:

Input: rowIndex = 1
Output: [1,1]

 

Constraints:

    0 <= rowIndex <= 33

"""
class Solution:
    def combination(self, p, q):
        return factorial(p)//(factorial(p-q)*factorial(q))

    def factorial(self, n):
        if n == 1 or n == 0:
            return 1
        return n * factorial(n-1)

    def getRow(self, rowIndex: int) -> List[int]:
        pascal_array = []
        j = 0
        for i in range(rowIndex+1):
            pascal_array.append(self.combination(rowIndex, i))
        return pascal_array
"""
The first solution makes use of the formula for calculating the nth row of a Pascal's triangle
https://www.geeksforgeeks.org/pascals-triangle-formula/
The second solution below is the iterative way whereby all rows are calculated and subsequent row derived until
we reach our desired row

"""

class Solution:

    def getRow(self, rowIndex: int) -> List[int]:
        
        if rowIndex < 1:
            return [1]
        new_row = [1]
        for i in range(1,rowIndex+1):
            last_row = new_row
            new_row = [1,1]
            
            for j in range(1, i):
                val = last_row[j-1] + last_row[j]
                new_row.insert(j, val)
        return new_row

        
    