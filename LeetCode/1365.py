class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        num_idx = []
        for i in range(len(nums)):
            num_idx.append([nums[i],i])
        num_idx = sorted(num_idx,key = lambda x:x[0])
        result = [0]*len(nums)
        for i in range(len(num_idx)):
            idx = num_idx[i][1]
            if i-1>=0 and num_idx[i][0]==num_idx[i-1][0]:
                p_idx = num_idx[i-1][1]
                result[idx] = result[p_idx]
            else:
                result[idx]=i
        return result

if __name__ == '__main__':
    so = Solution()
    print(so.smallerNumbersThanCurrent([6,3,7,6,9]))
