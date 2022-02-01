# Problem Link : https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

# Solution

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        lp = 999999
        bp = 0
        
        for price in prices:
            p = price - lp
            bp = max(p, bp)
            lp = min(price, lp)
        return bp
