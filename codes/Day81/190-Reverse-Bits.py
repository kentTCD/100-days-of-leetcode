class Solution:
    def reverseBits(self, n: int) -> int:
        res = ""
        for i in range(31, -1, -1):
            res = str(n // (2**i)) + res
            n = n % (2**i)
        return int(res, 2)

    ### Someone's solution
    def reverseBits(self, n: int) -> int:
        return int(str('{:032b}'.format(n))[::-1],2)