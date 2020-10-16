class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num_dict = {}
        longest_seq = 0
        for n in nums:
            num_dict[n] = 1
        for n in nums:
            if num_dict[n]>1:
                continue
            seq = self.__get_seq(n,num_dict)
            longest_seq = max(longest_seq,seq)
        return longest_seq

    def __get_seq(self,num,num_dict):
        if num-1 in num_dict:
            if num_dict[num-1]>1:
                num_dict[num] = num_dict[num-1] + num_dict[num]
            else:
                num_dict[num] = self.__get_seq(num-1,num_dict)+num_dict[num]
            return num_dict[num]
        else:
            return num_dict[num]



if __name__ == '__main__':
    so = Solution()
    print(so.longestConsecutive([100, 4, 200, 1, 3, 2]))