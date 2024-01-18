from functools import lru_cache
class Solution:
    def maxProfit(self, k, prices):
        @lru_cache(None)
        def dp(i, holding, remain):
            if i == len(prices) or remain == 0:
                return 0
            
            ans = dp(i + 1, holding, remain)
            print(ans)
            if holding:
                ans = max(ans, prices[i] + dp(i + 1, False, remain - 1))
            else:
                ans = max(ans, -prices[i] + dp(i + 1, True, remain))
                print(ans)
            
            return ans
        
        return dp(0, False, k)
s=Solution()
s.maxProfit(2,[2,4,1])