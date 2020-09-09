class Solution(object):
    def __init__(self):
        self.__result = [-1,-1]
        self.__find = False
        pass

    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        self.__subSearch(nums,0,len(nums)-1,target)
        return self.__result

    def __subSearch(self,nums,s_idx,e_idx,target):
        if self.__find:
            return
        if e_idx<s_idx:
            return
        mid = (s_idx+e_idx)//2
        if nums[mid]==target:
            self.__result[0]=mid
            self.__result[1]=mid
            self.__find=True
            i=1
            while mid-i>=0 and nums[mid-i]==target:
                    i+=1
            self.__result[0]=mid-i+1
            i = 1
            while mid + i <len(nums) and nums[mid+i]==target:
                    i += 1
            self.__result[1] = mid + i - 1
            return
        if nums[mid]>target:
            self.__subSearch(nums,s_idx,mid-1,target)
        else:
            self.__subSearch(nums,mid+1,e_idx,target)

if __name__ == '__main__':
    so = Solution()
    print(so.searchRange([5,7,7,8,8,10],6))