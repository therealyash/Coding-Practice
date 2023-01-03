"""
We define the usage of capitals in a word to be 
right when one of the following cases holds:
All letters in this word are capitals, like "USA". 
All letters in this word are not capitals, like "leetcode". 
Only the first letter in this word is capital, like "Google". 
Given a string word, return true if the usage of capitals 
in it is right.
"""

class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if word.isupper():
            return True
        elif word.islower():
            return True
        else:
            return False
s = input('Enter a String: ')
a = Solution()
print(a.detectCapitalUse(s))




