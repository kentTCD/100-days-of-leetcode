class Solution:
    ### My solution that couldn't escape from TimeLimitExceeded.
    def __init__(self):
        self.depth = 0
        self.mini = None
        self.tri = []
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        self.depth = len(triangle) - 1 # begin with 0
        if self.depth == 0:
            return triangle[0][0]
        self.tri = triangle
        def dfs(i, depth, cur_sum):
            if depth > self.depth:
                self.mini = min(self.mini, cur_sum) if self.mini is not None else cur_sum
                return
            for j in range(i, i+2):
                dfs(j, depth+1, cur_sum+self.tri[depth][j])


        dfs(0, 1, self.tri[0][0])
        return self.mini

    ### Someone's solution
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        memo = [[-1] * len(triangle) for _ in range(len(triangle))]
        def dfs(i, j):
            if i == len(triangle):
                return 0
            if memo[i][j] != -1:
                return memo[i][j]

            lower_left = triangle[i][j] + dfs(i + 1, j)
            lower_right = triangle[i][j] + dfs(i + 1, j + 1)
            memo[i][j] = min(lower_left, lower_right)
            return memo[i][j]

        return dfs(0, 0)