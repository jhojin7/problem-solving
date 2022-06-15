"""
ac:https://leetcode.com/submissions/detail/722949700/
help:https://leetcode.com/problems/longest-string-chain/discuss/1213876/Python-3-solutions-LIS-DP-Top-down-DP-Bottom-up-DP-Clean-and-Concise
"""
from __solver import *
class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        # sort words by length beforehand
        words.sort(key=len)
        #dp. counts chains
        dp = collections.OrderedDict()
        for word in words:
            dp[word] = 1 # checks chains
            for i in range(len(word)):
                # make a new word excluding a letter
                sub_word = word[:i] + word[i+1:]
                # ...and check if word in dp 
                if (sub_word in dp 
                    # and dp[word] is smaller
                    and dp[sub_word]+1 > dp[word]): 
                    # add count
                    dp[word] = dp[sub_word] + 1
        # find max chain count
        return max(dp.values())

tc = testcases("""
["xbc","pcxbcf","xb","cxbc","pcxbc"]
["a","b","ba","bca","bda","bdca"]
["abcd","dbqca"]
""")
while tc:
    print(Solution().longestStrChain(*tc.popleft()))