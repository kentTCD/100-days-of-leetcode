class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        n = len(mat)
        m = len(mat[0])
        if n * m != r * c:
            return mat
        new_mat = [[0] * c for _ in range(r)]
        
        col = row = 0
        for i in range(n):
            for j in range(m):
                if col == c:
                    col = 0
                    row += 1
                new_mat[row][col] = mat[i][j]
                col += 1
        return new_mat

