class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices)<2:
            return 0
        highest = prices[-1]
        benefit = 0
        for idx in range(len(prices)-2,-1,-1):
            benefit = max(benefit,highest-prices[idx])
            highest = max(highest,prices[idx])
        return benefit

if __name__ == '__main__':
    so = Solution()
    print(so.maxProfit([7,6,4,3,1]))