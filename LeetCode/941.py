class Solution(object):
    def validMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        len_a = len(A)
        if len_a<3:
            return False
        l_sum = [0 for a in A]
        r_sum = [0 for a in A]
        for i in range(1,len_a):
            if A[i]>A[i-1]:
                l_sum[i]=l_sum[i-1]+1
        for i in range(len_a-2,-1,-1):
            if A[i] > A[i + 1]:
                r_sum[i] = r_sum[i + 1] + 1

        for i in range(1,len_a-1):
            if l_sum[i]==i and r_sum[i]==len_a-i-1:
                return True
        return False

if __name__ == '__main__':
    so = Solution()
    A = [2,1]
    print(so.validMountainArray(A))
