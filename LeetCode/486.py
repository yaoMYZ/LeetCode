class Solution(object):
    def __init__(self):
        pass

    def PredictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        num = self.__subPredict(nums,0)
        if num>=0:
            return True
        else:
            return False

    def __subPredict(self,nums,p_id):
        if len(nums)==1:
            if p_id==1:
                return -nums[0]
            else:
                return nums[0]
        num1 = self.__subPredict(nums[1:],(p_id + 1) % 2)
        if p_id == 1:
            num1 -= nums[0]
        else:
            num1 += nums[0]
        num2 = self.__subPredict(nums[:-1], (p_id + 1) % 2)
        if p_id == 1:
            num2 -= nums[-1]
        else:
            num2 += nums[-1]

        if p_id==1:
            return min([num1,num2])
        else:
            return max([num1,num2])


if __name__ == '__main__':
    so = Solution()
    print(so.PredictTheWinner([1, 5, 2]))