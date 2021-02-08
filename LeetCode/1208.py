class Solution:
    def equalSubstring(self, s, t, maxCost):
        n = len(s)
        diff = [abs(ord(sc) - ord(tc)) for sc, tc in zip(s, t)]
        maxLength = start = end = 0
        total = 0

        while end < n:
            total += diff[end]
            while total > maxCost:
                total -= diff[start]
                start += 1
            maxLength = max(maxLength, end - start + 1)
            end += 1

        return maxLength


if __name__ == '__main__':
    so = Solution()
    s = "vjlqwkzamvyv"
    t = "suusjpqkhlkz"
    cost = 7
    print(so.equalSubstring(s,t,cost))
