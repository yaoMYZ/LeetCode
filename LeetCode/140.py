import copy
from functools import lru_cache

class Solution:
    def wordBreak(self, s, wordDict):
        @lru_cache(None)
        def backtrack(index):
            if index == len(s):
                return [[]]
            ans = list()
            for i in range(index + 1, len(s) + 1):
                word = s[index:i]
                if word in wordSet:
                    nextWordBreaks = backtrack(i)
                    for nextWordBreak in nextWordBreaks:
                        ans.append(copy.deepcopy(nextWordBreak)+ [word])
            return ans

        wordSet = set(wordDict)
        breakList = backtrack(0)
        return [" ".join(words[::-1]) for words in breakList]


if __name__ == '__main__':
    so = Solution()
    s = "pineapplepenapple"
    wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
    print(so.wordBreak(s,wordDict))

