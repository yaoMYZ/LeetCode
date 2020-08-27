class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        nums = {'2':['a','b','c'],'3':['d','e','f'],'4':['g','h','i'],'5':['j','k','l'],'6':['m','n','o'],'7':['p','q','r','s'],
                '8':['t','u','v'],'9':['w','x','y','z']}
        if len(digits)<1:
            return []
        all_char = []
        for char in nums[digits[0]]:
            all_char.append([char])
        for d in digits[1:]:
            new_char = []
            for char_arr in all_char:
                for char in nums[d]:
                    tmp_char = char_arr + [char]
                    new_char.append(tmp_char)
            all_char = new_char

        combiantions = set()
        result = []
        for char_arr in all_char:
            sorted(char_arr)
            char_arr = tuple(char_arr)
            if char_arr not in combiantions:
                combiantions.add(char_arr)
                tmp_str = ''
                for char in char_arr:
                    tmp_str+=char
                result.append(tmp_str)
        return result

if __name__ == '__main__':
    nums = "23"
    solution = Solution()
    coms = solution.letterCombinations(nums)
    print(coms)

