class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0: return []
        letters = {
            '2':['a', 'b', 'c'],
            '3':['d', 'e', 'f'],
            '4':['g', 'h', 'i'],
            '5':['j', 'k', 'l'],
            '6':['m', 'n', 'o'],
            '7':['p', 'q', 'r', 's'],
            '8':['t', 'u', 'v'],
            '9':['w', 'x', 'y', 'z']
        }
        rtn_ltrs = []
        len_digi = len(digits)
        def dfs(digits, path):
            if len(path) == len_digi:
                return rtn_ltrs.append(path)
            
            left = digits[0]
            for v in letters[left]:
                dfs(digits[1:], path + v)
            
        dfs(digits, '')
        
        return rtn_ltrs