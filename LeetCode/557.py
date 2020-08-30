class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        ss = s.split(' ')
        result = ss[0][::-1]
        for t_s in ss[1:]:
            result += ' '+t_s[::-1]
        return result

if __name__ == '__main__':
    so = Solution()
    print(so.reverseWords("Let's take LeetCode contest"))