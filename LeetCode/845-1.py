class Solution(object):
    def longestMountain(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if len(A)==0:
            return 0
        seq1 = [1]*len(A)
        for idx in range(1,len(A)):
            if A[idx]>A[idx-1]:
                seq1[idx]=seq1[idx-1]+1
        seq2 = [1]*len(A)
        for idx in range(len(A)-2, -1, -1):
            if A[idx] > A[idx + 1]:
                seq2[idx]=seq2[idx+1]+1
        num = 0
        for s1,s2 in zip(seq1,seq2):
            if s1>=2 and s2>=2:
                num = max(num,s1+s2-1)
        return num

if __name__ == '__main__':
    so = Solution()
    print(so.longestMountain([2,2,2]))