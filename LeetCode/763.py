class Solution(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        chars_dict={}
        for i in range(len(S)):
            if S[i] not in chars_dict:
                chars_dict[S[i]] = -1
            chars_dict[S[i]] = i
        result=[]
        i = 0
        while i<len(S):
            start_idx = i
            max_i = chars_dict[S[i]]
            tmp_char_set = set()
            tmp_char_set.add(S[i])
            j=i+1
            while j<=max_i:
                tmp_char_set.add(S[j])
                if chars_dict[S[j]]>max_i:
                    max_i = chars_dict[S[j]]
                j+=1
            result.append(j-start_idx)
            i=j
        return result

if __name__ == '__main__':
    so = Solution()
    S = "ababcbacadefegdehijhklij"
    print(so.partitionLabels(S))
