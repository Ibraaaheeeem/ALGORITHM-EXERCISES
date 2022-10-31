class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:

        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        i = 0
        j = 0

        for i in range(n):
            num = nums2[i]
            j = 0
            for j in range(m + n):
                print(j)
                if nums1[i] == 0 and j > 
                if nums1[j] > num:
                    print("{} - {} - {}".format(i, j, num))
                    nums1.insert(j, num)
                    nums1.pop()
                    break;