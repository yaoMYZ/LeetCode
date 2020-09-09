class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        tmp_stack = [-1]
        maxlen = 0
        for i in range(len(s)):
            t_s = s[i]
            if t_s=='(':
                tmp_stack.append(i)
            else:
                tmp_stack.pop()
                if len(tmp_stack)==0:
                    tmp_stack.append(i)
                else:
                    maxlen = max(maxlen,i-tmp_stack[-1])
        return maxlen

if __name__ == '__main__':
    so = Solution()
    print(so.longestValidParentheses("()(()"))