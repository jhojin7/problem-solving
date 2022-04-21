'''
https://leetcode.com/submissions/detail/678159563/
'''
import collections
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        # pythonic way
        # return sum(stone in jewels for stone in stones)

        # # python counter
        # stones_cnt = collections.Counter(stones)
        stones_cnt = collections.defaultdict(stones)
        print(stones_cnt)
        ret = 0
        for ch in jewels:
            ret += stones_cnt[ch]
        return ret

        # hashing with dict
        stones_cnt = {}
        for stone in stones:
            if stone not in stones_cnt:
                stones_cnt[stone] = 1
            else:
                stones_cnt[stone] += 1
        ret = 0
        for jewel in jewels:
            ret += stones_cnt[jewel]
        return ret
            

jewels = "aA"
stones = "aAAbbbb"
# jewels = "z"
# stones = "ZZ"
sol = Solution.numJewelsInStones(Solution,jewels,stones)
print(sol)