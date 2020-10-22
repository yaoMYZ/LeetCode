class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        neg_idxs = []
        s_idx = 0
        max_product = -10e10
        zeros_num = 0
        for i in range(len(nums)):
            if nums[i]<0:
                neg_idxs.append(i)
            if nums[i]==0:
                zeros_num+=1
                max_product=max(max_product,self.__get_max_product(neg_idxs,nums,s_idx,i))
                s_idx=i+1
                neg_idxs=[]
        max_product = max(max_product, self.__get_max_product(neg_idxs, nums,s_idx,len(nums)))
        if max_product<0 and zeros_num>0:
            return 0
        return max_product

    def __get_max_product(self,neg_idxs,nums,s_idx,e_idx):
        if s_idx >= e_idx:
            return 0
        if len(neg_idxs)%2==0:
            return self.__product(nums,s_idx,e_idx)
        p1 = self.__product_1area(neg_idxs[-1],nums,s_idx,neg_idxs[-1])
        p2 = self.__product_1area(neg_idxs[-1], nums, neg_idxs[-1]+1,e_idx)
        p3 = self.__product_1area(neg_idxs[0], nums, s_idx, neg_idxs[0])
        p4 = self.__product_1area(neg_idxs[0], nums, neg_idxs[0] + 1, e_idx)
        return max(p1,p2,p3,p4)

    def __product_1area(self,neg_idx,nums,s_idx,e_idx):
        if s_idx>=e_idx:
            return nums[neg_idx]
        else:
            return self.__product(nums,s_idx,e_idx)

    def __product(self,nums,s_idx,e_idx):
        p = 1
        for i in range(s_idx, e_idx):
            p *= nums[i]
        return p

if __name__ == '__main__':
    so = Solution()
    print(so.maxProduct([2,3,-2,4]))