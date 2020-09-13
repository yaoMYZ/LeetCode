class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        str_dict = {}
        for str in strs:
            tmp = tuple(sorted(str))
            if tmp not in str_dict:
                str_dict[tmp] = []
            str_dict[tmp].append(str)
        return str_dict.values()

if __name__ == '__main__':
    so = Solution()
    strs = ["",""]
    print(so.groupAnagrams(strs))