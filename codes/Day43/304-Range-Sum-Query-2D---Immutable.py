class NumMatrix:
    ### Someone's solution
    #T=O(m*n), S=O(m*n); m=rows, n=cols
    def __init__(self, matrix: List[List[int]]):
        rows, cols = len(matrix), len(matrix[0])
        self.prefixSum = [[0]*(cols+1) for _ in range(rows+1)]
        for r in range(1, rows+1):
            for c in range(1, cols+1):
                self.prefixSum[r][c] = self.prefixSum[r-1][c] + self.prefixSum[r][c-1] - self.prefixSum[r-1][c-1] + matrix[r-1][c-1]
    #T=O(1), S=O(1)
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        r1, c1, r2, c2 = row1+1, col1+1, row2+1, col2+1
        return self.prefixSum[r2][c2] - self.prefixSum[r2][c1-1] - self.prefixSum[r1-1][c2] + self.prefixSum[r1-1][c1-1]

# class NumMatrix:
### My solution that faced Time Limit Error
#     def __init__(self, matrix: List[List[int]]):
#         self.matrix = matrix
#         self.row_sums = [sum(row) for row in matrix]
#         self.len_row = len(matrix[0] )

#     def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
#         res_sum = 0
#         for row_id in range(row1, row2+1):
#             res_sum += (self.row_sums[row_id] - (sum(self.matrix[row_id][:col1]) + sum(self.matrix[row_id][col2+1:self.len_row])))
#         return res_sum


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)