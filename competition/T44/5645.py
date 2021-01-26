class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        result = [0]
        maxh = 0
        for i in range(len(gain)):
            tmp = gain[i]+result[i]
            result.append(tmp)
            maxh = max(maxh,tmp)
        return maxh

if __name__ == '__main__':
    so = Solution()
    gain = [-4,-3,-2,-1,4,3,2]
    re = so.largestAltitude(gain)
    print(re)