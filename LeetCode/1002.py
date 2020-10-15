import numpy as np
class Solution(object):
    def commonChars(self, A):
        """
        :type A: List[str]
        :rtype: List[str]
        """
        char_dict = {}
        char_num = len(A)
        for idx in range(char_num):
            for c in A[idx]:
                if c not in char_dict:
                    char_dict[c] = np.zeros(char_num,dtype=np.int)
                char_dict[c][idx]+=1
        result = []
        for key,values in char_dict.items():
            num = int(np.min(values))
            result+=[key for i in range(num)]
        return result

if __name__ == '__main__':
    so = Solution()
    A = ["cool","lock","cook"]
    print(so.commonChars(A))
