"""
https://leetcode.com/submissions/detail/718600912/
https://leetcode.com/problems/longest-substring-without-repeating-characters/discuss/1812/Share-my-Java-solution-using-HashSet
"""
from __solver import *
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # set of characters in a substring. no repeat
        chars = set() # 3 3 {'c', 'b', 'a'}
        # left, right: pointers
        left, right = 0, 0
        # maxlen: longest substring length
        maxlen = 0

        while right < len(s):
            # print(maxlen,len(chars),chars)
            # check if s[right] is in set
            if s[right] not in chars:
                # if not, add to set
                # and move right forward
                chars.add(s[right])
                right += 1
                maxlen = max(maxlen,len(chars))
            else:
                # if char in set, remove s[left] 
                # and move left forward
                chars.remove(s[left])
                left += 1
        return maxlen

tc = testcases("""
"abcabcbb"
"bbbbb"
"pwwkew"
""
""")
# "aaaaffffffabbbbbcccdddra08asdf88888a"
while tc: 
    print(Solution().lengthOfLongestSubstring(*tc.popleft()))