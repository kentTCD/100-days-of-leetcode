class Solution:
    ### My solution that couldn't pass because of memory limit exceed.
    def __init__(self):
        self.mat = []
        self.num_mat = 0
        self.hash = {}
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        self.mat = mat
        self.num_m = len(mat)
        self.num_n = len(mat[0])
        res = [[] for _ in range(self.num_m)]
        
        def dfs(m, n, dis):
            neighbors = [(m-1, n), (m+1, n), (m, n-1), (m, n+1)]
            for nbr in neighbors:
                m, n = nbr[0], nbr[1]
                if m < 0 or m >= self.num_m or n < 0 or n >= self.num_n:
                    continue
                if self.mat[m][n] == 0:
                    return dis
            # if not return
            dises = []
            for nbr in neighbors:
                m, n = nbr[0], nbr[1]
                if m < 0 or m >= self.num_m or n < 0 or n >= self.num_n:
                    continue
                if self.hash.get(f'{m},{n}'):
                    dises.append(self.hash[f'{m},{n}'] + 1)
                else:
                    dises.append(dfs(m, n, dis+1))
            return min(dises)
        for m in range(self.num_m):
            for n in range(self.num_n):
                if mat[m][n] == 0:
                    res[m].append(0)
                    self.hash[f'{m},{n}'] = 0
                else:
                    val = dfs(m, n, 1)
                    res[m].append(val)
                    self.hash[f'{m},{n}'] = val
        return res


    ### Someone's solution that I learned from.
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        row = len(mat)
        col = len(mat[0])
        queue = deque()

        for i in range(row):
            for j in range(col):
                if mat[i][j] == 0:
                    queue.append((i, j))
                    
        visited = set()
        visited.update(queue)
    
        count = 0
        
        # BFS
        while queue:
            for _ in range(len(queue)):
                x, y = queue.popleft()
                for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    xx, yy = x + dx, y + dy
                    if xx < 0 or xx == row or yy < 0 or yy == col:
                        continue
                    if (xx, yy) in visited:
                        continue
                    queue.append((xx, yy))
                    visited.add((xx, yy))
                if mat[x][y] == 0:
                    mat[x][y] = 0
                else:
                    mat[x][y] = mat[x][y] + count - 1
            count += 1
            
        return mat