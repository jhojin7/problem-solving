"""
https://leetcode.com/submissions/detail/711013741/
"""
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)