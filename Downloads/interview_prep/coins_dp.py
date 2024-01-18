from functools import lru_cache
class Solution:
    def coinChange(self, coins, amount):
       
        @lru_cache(None)
        def dp(i):
            if i<0:
                return -1
            if i==0:
                return 0
            min_cost=float("inf")
            for coin in coins:
                res=dp(i-coin)
                
                if res!=-1:
                    print(i,res)
                    min_cost=min(min_cost,res+1)
            return -1 if min_cost==float("inf") else min_cost
        return dp(amount)
s=Solution()
print(s.coinChange([1,2,5],11))