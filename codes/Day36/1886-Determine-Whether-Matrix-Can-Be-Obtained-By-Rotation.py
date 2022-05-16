class Solution:
    def __init__(self):
        self.bool = False
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        if mat == target: return True

        def rotate_90(mat, target, try_num):
            if try_num > 3:
                self.bool = False
                return
            rotated = [[] for x in range(len(mat))]
            for row in reversed(mat):
                for i in range(len(row)):
                    rotated[i].append(row[i])
            if rotated == target:
                self.bool = True
                return
            rotate_90(rotated, target, try_num+1)

        rotate_90(mat, target, 1)
        return self.bool