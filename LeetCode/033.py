class Solution(object):
    def __init__(self):
        self.__target_idx = -1

    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums)==0:
            return self.__target_idx
        self.__subSearch(nums,0,len(nums)-1,target)
        return self.__target_idx

    def __subSearch(self,nums,s_idx,e_idx,target):
        if self.__target_idx!=-1:
            return
        if e_idx<s_idx:
            return
        if s_idx==e_idx:
            if nums[s_idx]==target:
                self.__target_idx=s_idx
            return
        mid = (s_idx+e_idx)//2
        if nums[mid]==target:
            self.__target_idx=mid
            return
        if nums[mid]>nums[-1]:
            if nums[mid]<target:
                self.__subSearch(nums,mid+1,e_idx,target)
            else:
                if nums[s_idx]==target:
                    self.__target_idx=s_idx
                    return
                if nums[s_idx]>target:
                    self.__subSearch(nums, mid + 1, e_idx, target)
                else:
                    self.__subSearch(nums,s_idx,mid-1,target)
        else:
            if nums[mid]<target:
                if nums[e_idx]==target:
                    self.__target_idx=e_idx
                    return
                if nums[e_idx]<target:
                    self.__subSearch(nums, s_idx, mid - 1, target)
                else:
                    self.__subSearch(nums, mid + 1, e_idx, target)
            else:
                self.__subSearch(nums, s_idx,mid-1, target)


if __name__ == '__main__':
    nums = [1,3]
    target = 0
    so = Solution()
    print(so.search(nums,target))