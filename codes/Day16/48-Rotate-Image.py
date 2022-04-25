class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if len(matrix) == 1: return

        for i in range(len(matrix)):
            for j in range(len(matrix)):
                target = j + (len(matrix[i]) - len(matrix))
                move_num = matrix[i].pop(target)
                matrix[j] = [move_num] + matrix[j]