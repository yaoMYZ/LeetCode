class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        s = sum(nums[:k])
        m_s = s
        for i in range(k,len(nums)):
            s = s-nums[i-k]+nums[i]
            m_s = max(s,m_s)
        return m_s/float(k)

if __name__ == '__main__':
    so = Solution()
    nums = [1,12,-5,-6,50,3]
    k = 4
    print(so.findMaxAverage(nums,k))