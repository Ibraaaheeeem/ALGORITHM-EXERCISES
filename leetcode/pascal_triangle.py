class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows < 1:
            return None
        pascal_triangle = []
        pascal_triangle.append([1])
        for i in range(1,numRows):
            
            pascal_triangle.append([1])
            pascal_triangle[i].append(1)
            for j in range(1, i):
                
                val = pascal_triangle[i-1][j-1] + pascal_triangle[i-1][j]
                pascal_triangle[i].insert(j, val)
        return pascal_triangle

