from __solver import *
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        ans = 0
        coins = sorted(coins)#,reverse=True)
        for coin in coins:
            print("coin",coin)
            print("ans",ans, amount, amount//coin, amount%coin)
            ans += amount//coin
            amount = amount%coin
        print(amount, ans)
        if amount != 0:
            return -1
        return ans


# [1,2,5]
# 11
# [2]
# 3
# [1]
# 0
# Solution.coinChange(Solution,[1,2,5],15)
# ret = Solution.coinChange(Solution,[2],3)
# ret = Solution.coinChange(Solution,[1],0)

# [186,419,83,408]
# 6249
ret = Solution.coinChange(Solution,[186,419,83,408],6249)
print(ret)
