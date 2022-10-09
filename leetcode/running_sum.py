
# Given an array nums. We define a running sum of an array as 
# runningSum[i] = sum(nums[0]…nums[i]).
# Return the running sum of nums.
class Solution:
    def running_sum(self, num_list: List[int]) -> List[int]:
        running_sum_list = []
        current_sum = 0
        for num in num_list:
            current_sum = current_sum + num
            running_sum.append(current_sum)
        return running_sum