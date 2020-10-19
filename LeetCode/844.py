class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        S = self.__get_char_stack(S)
        T = self.__get_char_stack(T)
        if len(S)!=len(T):
            return False
        for s,t in zip(S,T):
            if s!=t:
                return False
        return True

    def __get_char_stack(self,chars):
        tmp_stack = []
        for c in chars:
            if c!='#':
                tmp_stack.append(c)
            elif len(tmp_stack)>0:
                tmp_stack.pop(-1)
        return tmp_stack

if __name__ == '__main__':
    so = Solution()
    print(so.backspaceCompare("a##c","#a#c"))