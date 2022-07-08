class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        def searchFreshAndRotten(grid):
            freshes = 0
            rots = []
            for row in range(len(grid)):
                for col in range(len(grid[row])):
                    if grid[row][col] == 1:
                        freshes += 1
                    elif grid[row][col] == 2:
                        rots.append((row, col))
            return freshes, rots

        freshes, nexts = searchFreshAndRotten(grid)
        len_r, len_c = len(grid), len(grid[0])
        minute = 0
        while freshes > 0 and len(nexts) > 0:
            rots = []
            for row, col in nexts:
                for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    x, y = row + dx, col + dy
                    if x < 0 or x == len_r or y < 0 or y == len_c:
                        continue
                    if grid[x][y] == 1:
                        grid[x][y] = 2
                        rots.append((x, y))
                        freshes -= 1
            nexts = rots
            minute += 1

        if freshes <= 0:
            return minute
        else:
            return -1