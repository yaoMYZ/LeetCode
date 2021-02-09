class Solution(object):
    def subarraysWithKDistinct(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        return self.atMostKDistinct(A, K) - self.atMostKDistinct(A, K - 1)

    def atMostKDistinct(self, A, K):
        length = len(A)
        freq = [0]* (length + 1)

        left = 0
        right = 0
        # [left, right) 里不同整数的个数
        count = 0
        res = 0
        # [left, right) 包含不同整数的个数小于等于 K
        while right < length:
            if freq[A[right]] == 0:
                count+=1
            freq[A[right]]+=1
            right+=1

            while count > K:
                freq[A[left]]-=1
                if freq[A[left]] == 0:
                    count-=1
                left+=1
            # [left, right) 区间的长度就是对结果的贡献
            res += right - left
        return res

