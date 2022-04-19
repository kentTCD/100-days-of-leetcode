class Solution:
    def countBits(self, n: int) -> List[int]:
        if n == 0: return [0]
        rtn_list = []
        for i in range(n+1):
            rtn_list.append(str(bin(i)).count('1'))

        return rtn_list