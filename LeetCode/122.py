class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices)==0:
            return 0
        sbuy = -prices[0]
        ssell = 0
        for p in prices[1:]:
            t_sbuy = sbuy
            sbuy = max(sbuy,ssell-p)
            ssell = max(ssell,p+t_sbuy)
        return ssell

if __name__ == '__main__':
    so = Solution()
    prices = [7,6,4,3,1]
    print(so.maxProfit(prices))
