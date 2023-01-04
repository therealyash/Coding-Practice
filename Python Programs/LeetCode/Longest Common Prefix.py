"""
Write a function to find the longest common
prefix string amongst an array of strings.
If there is no common prefix, return an empty string
"""

class Solution:
    def longestCommonPrefix(self, strs):

        if not strs:
            return ""
        shortest = min(strs,key=len)
        for i, ch in enumerate(shortest):
            for other in strs:
                if other[i] != ch:
                    return shortest[:i]
        return shortest

strs = ["flower","flow","flight"]
obj = Solution()
print(obj.longestCommonPrefix(strs))