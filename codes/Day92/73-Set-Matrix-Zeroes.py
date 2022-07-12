class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        len_x = len(matrix)
        len_y = len(matrix[0])
        zeros_x, zeros_y = [], []
        for x in range(len_x):
            for y in range(len_y):
                if matrix[x][y] == 0:
                    zeros_x.append(x)
                    zeros_y.append(y)
        for x in set(zeros_x):
            matrix[x] = [0] * len_y
        for y in set(zeros_y):
            for x in range(len_x):
                matrix[x][y] = 0