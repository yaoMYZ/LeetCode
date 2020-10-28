class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        num_dict = {}
        for n in arr:
            if n not in num_dict:
                num_dict[n]=0
            num_dict[n]+=1
        num_set = set()
        for _,n in num_dict.items():
            if n not in num_set:
                num_set.add(n)
            else:
                return False
        return True