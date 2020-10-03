import collections

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_idx = collections.defaultdict()
        for i,n in enumerate(nums):
            num_idx[n] = i
        num=[]
        for i, n in enumerate(nums):
            num=[i]
            diff = target-n
            if diff in num_idx and num_idx[diff]!=i:
                num.append(num_idx[diff])
                break
        return num

if __name__ == '__main__':
    nums = [3,2,4]
    tar = 6
    so = Solution()
    print(so.twoSum(nums,tar))