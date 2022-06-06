class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        res = 0
        digi = 0
        for i in range(len(columnTitle)-1, -1, -1):
            # Base 26
            res += (ord(columnTitle[i])-64)*(26**digi)
            digi += 1
        return res