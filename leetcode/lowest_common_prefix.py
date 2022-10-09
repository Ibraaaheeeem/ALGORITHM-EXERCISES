"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

"""
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        lcp = ""
        j = 0
        for i in range(0, len(strs[0])):
            lcp = strs[0][:i+1]
            for j in range(0, len(strs)):
                if not strs[j].startswith(lcp):
                    return lcp[:-1]
                else:
                    continue
        return lcp
                
            