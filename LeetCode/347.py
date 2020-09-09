from heapq import *

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        num_count = dict()
        for num in nums:
            if num not in num_count:
                num_count[num]=0
            num_count[num]+=1
        result = []
        for key, value in num_count.items():
            result.append([value,key])
        heapify(result)
        f_result = [k for v, k in nlargest(k,result)]
        return f_result

if __name__ == '__main__':
    nums = [1,1,1,2,2,3]
    k = 2
    so = Solution()
    print(so.topKFrequent(nums,k))