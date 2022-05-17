class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if len(matrix[0]) == 1:
            return [row[0] for row in matrix]
        res = []
        def go_straight(matrix, prev_act=None):
            j = 0
            for i, row in enumerate(matrix.copy()):
                if len(row) == 0:
                    matrix.pop(i-j)
                    j += 1
            if len(matrix) == 0:
                return
            if prev_act == 'up' or prev_act is None:
                for num in matrix[0]:
                    res.append(num)
                matrix.pop(0)
                go_straight(matrix, 'right')
            elif prev_act == 'right':
                for row in matrix:
                    res.append(row.pop())
                go_straight(matrix, 'down')
            elif prev_act == 'down':
                for num in reversed(matrix[-1]):
                    res.append(num)
                matrix.pop()
                go_straight(matrix, 'left')
            elif prev_act == 'left':
                for row in reversed(matrix):
                    res.append(row.pop(0))
                go_straight(matrix, 'up')
        go_straight(matrix)
        return res