class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        wordSet = set()
        for word in wordDict:
            wordSet.add(word)
        dp = [False for i in range(len(s)+1)]
        dp[0] = True
        for i in range(1,len(s)+1):
            for j in range(i):
                if dp[j] and s[j:i] in wordSet:
                    dp[i] = True
                    break
        return dp[len(s)]


if __name__ == '__main__':
    so = Solution()
    print(so.wordBreak("catsandog",["cats", "dog", "sand", "and", "cat"]))