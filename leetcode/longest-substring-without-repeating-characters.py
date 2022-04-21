import collections


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        print(s)
        maxlen, start = 0, 0
        not_ret = {}
        for i,ch in enumerate(s):
            print(i,ch)
            if ch not in not_ret:
                not_ret[ch] = i




        
s = "abcabcabc"
Solution.lengthOfLongestSubstring(Solution,s)