class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        res_product = 1
        res_sum = 0
        str_n = str(n)
        for i in range(len(str_n)):
            res_product *= int(str_n[i])
            res_sum += int(str_n[i])
        return res_product - res_sum