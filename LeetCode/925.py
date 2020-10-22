class Solution(object):
    def isLongPressedName(self, name, typed):
        """
        :type name: str
        :type typed: str
        :rtype: bool
        """
        n_idx = 0
        n_len = len(name)
        t_idx = 0
        t_len = len(typed)
        while n_idx<n_len:
            if t_idx>=t_len:
                return False
            if name[n_idx]==typed[t_idx]:
                n_idx+=1
                t_idx+=1
            elif n_idx-1>=0 and name[n_idx-1]==typed[t_idx]:
                t_idx+=1
            else:
                return False
        if t_idx<t_len:
            while t_idx<t_len:
                if name[n_len - 1] == typed[t_idx]:
                    t_idx += 1
                else:
                    return False
        return True

if __name__ == '__main__':
    so = Solution()
    name = "alex"
    typed = "alexxr"
    print(so.isLongPressedName(name,typed))