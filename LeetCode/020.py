class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        tmp_arr = []
        for t_s in s:
            if self.__if_left(t_s):
                tmp_arr.append(t_s)
            else:
                if len(tmp_arr)==0:
                    return False
                if not self.__match(tmp_arr[-1],t_s):
                    return False
                else:
                    tmp_arr.pop(-1)
        if len(tmp_arr)>0:
            return False
        else:
            return True

    def __if_left(self,char):
        if char=='(' or char=='[' or char=='{':
            return True
        else:
            return False

    def __match(self,t_s,s):
        if t_s=='(' and s==')':
            return True
        if t_s=='[' and s==']':
            return True
        if t_s=='{' and s=='}':
            return True

if __name__ == '__main__':
    s ="(]"
    so =Solution()
    print(so.isValid(s))