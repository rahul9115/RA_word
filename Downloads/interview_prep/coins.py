class Solution:
    def coinChange(self, coins, amount):
        n = len(coins)

        def dfs(idx, amount):
            
            if amount == 0:
                return 0
            if idx < n and amount > 0:
                min_cost = float('inf')
                for x in range(0, amount // coins[idx] + 1):
                    res = dfs(idx + 1, amount-x * coins[idx])
                    print(res,amount)
                    if res != -1:
                        min_cost = min(min_cost, res + x)
                return -1 if min_cost == float('inf') else min_cost
            return -1

        return dfs(0, amount)
s=Solution()
print(s.coinChange([1,2,5],11))