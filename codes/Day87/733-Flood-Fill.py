class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        num_m = len(image)
        num_n = len(image[0])
        start = image[sr][sc]
        if start == color:
            return image
        
        def dfs(m, n):
            nonlocal image
            image[m][n] = color
            neighbors = [(m-1, n), (m+1, n), (m, n-1), (m, n+1)]
            for nbr in neighbors:
                m, n = nbr[0], nbr[1]
                if (m < 0 or m >= num_m or n < 0 or n >= num_n):
                    continue
                if image[m][n] == start:
                    dfs(m, n)

        dfs(sr, sc)
        return image