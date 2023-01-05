"""
Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:

'.' Matches any single character.​​​​
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).
"""

import re
class Solution:
    # @return a boolean
    def isMatch(self, s, p):
        pattern = re.compile("^" + p + "$")
        if pattern.search(s) is None:
            return False
        return True





