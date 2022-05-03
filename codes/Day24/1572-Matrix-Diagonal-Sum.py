class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        sum_dia = 0
        for i in range(len(mat)):
            pri_dia = mat[i][i]
            sec_dia = 0 if len(mat)%2 == 1 and i == len(mat)//2 else mat[i][(i+1)*(-1)]
            sum_dia += (pri_dia + sec_dia)
        return sum_dia