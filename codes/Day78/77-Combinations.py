class Solution:
	def combine(self, n: int, k: int) -> List[List[int]]:
		res = []
		comb = []
		def dfs(i):

			if len(comb) == k:
				res.append(comb.copy())
				return 
			for j in range(i,n+1):
				comb.append(j)
				dfs(j+1)
				comb.pop()
		dfs(1)
		return res