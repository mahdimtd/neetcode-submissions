class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        left  = 0
        right = left+1 
        best = 0
        for _ in range(len(prices)-1):
            if prices[left] >= prices[right]:
                left = right
                right += 1   
            elif prices[left] < prices[right]:
                best = max(best,prices[right] - prices[left])
                right += 1   


        return best
