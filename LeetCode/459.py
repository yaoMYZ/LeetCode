class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if_repeat = False
        str_l = len(s)
        for i in range(1,str_l//2+1):
            s_idx = 0
            e_idx = i
            interval = e_idx-s_idx
            if(str_l%interval==0):
                tmp_flag = True
                for j in range(i,str_l,interval):
                    if s[s_idx:e_idx]!=s[j:j+interval]:
                        tmp_flag=False
                        break
                if(tmp_flag):
                    if_repeat = tmp_flag
                    break
        return if_repeat



if __name__ == '__main__':
    solution = Solution()
    print(solution.repeatedSubstringPattern("babbabbabbabbab"))