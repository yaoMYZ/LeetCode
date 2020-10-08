class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        slen = len(s)
        for i in range(slen//2):
            tmp = s[i]
            s[i] = s[slen-i-1]
            s[slen-i-1] = tmp

if __name__ == '__main__':
    so = Solution()
    s = ["H","a","n","n","a","h"]
    so.reverseString(s)
    print(s)