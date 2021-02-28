class Solution(object):
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        flag = 0
        i = 1
        while i<len(A) and flag==0:
            if A[i]-A[i-1]>0:
                flag=1
            elif A[i]-A[i-1]<0:
                flag=-1
            i+=1

        if flag>0:
            for j in range(i,len(A)):
                if A[j]-A[j-1]<0:
                    return False
        else:
            for j in range(i,len(A)):
                if A[j]-A[j-1]>0:
                    return False
        return True

if __name__ == '__main__':
    so = Solution()
    A = [5,3,2,4,1]
    print(so.isMonotonic(A))