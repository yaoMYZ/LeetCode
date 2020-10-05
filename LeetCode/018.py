class Solution(object):
    def __init__(self):
        self.__coms = set()

    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if len(nums)<4:
            return []

        for i,num1 in enumerate(nums[:-3]):
            for j in range(i+1,len(nums)-2):
                num2 = nums[j]
                self.__findComs([num1,num2],target-num1-num2,nums[j+1:])
        return list(self.__coms)

    def __findComs(self,first_two,target,nums):
        num_dix = {}
        for i,n in enumerate(nums):
            if n not in num_dix:
                num_dix[n] = 0
            num_dix[n]+=1

        for n in nums:
            diff = target-n
            num_dix[n] -= 1
            if diff in num_dix and num_dix[diff]>0:
                nums = tuple(sorted(first_two+[n,diff]))
                if nums not in self.__coms:
                    self.__coms.add(nums)
                    num_dix[diff] -= 1

if __name__ == '__main__':
    so = Solution()
    nums = [-3,-1,0,2,4,5]
    target = 0
    print(so.fourSum(nums,target))