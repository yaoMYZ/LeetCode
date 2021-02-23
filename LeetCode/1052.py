class Solution(object):
    def maxSatisfied(self, customers, grumpy, X):
        """
        :type customers: List[int]
        :type grumpy: List[int]
        :type X: int
        :rtype: int
        """
        re = 0
        n_len = len(customers)
        for i in range(n_len):
            if grumpy[i]==0:
                re+=customers[i]
                customers[i]=0

        sidx = 0
        one_sum = 0
        while sidx<n_len and customers[sidx] == 0:
            sidx += 1
        eidx = sidx+X
        eidx = min(eidx,n_len)
        for i in range(sidx,eidx):
            one_sum+=customers[i]
        m_sum = one_sum

        while eidx<n_len:
            one_sum -= customers[sidx]
            sidx+=1
            add_t = 1
            while sidx<n_len and customers[sidx]==0:
                sidx+=1
                add_t+=1
            t_eidx = eidx + add_t
            t_eidx = min(t_eidx, n_len)
            for i in range(eidx, t_eidx):
                one_sum += customers[i]
            eidx = t_eidx
            m_sum = max(m_sum,one_sum)
        return re+m_sum

if __name__ == '__main__':
    so = Solution()
    customers = [1]
    grumpy = [0]
    X = 1
    print(so.maxSatisfied(customers,grumpy,X))


