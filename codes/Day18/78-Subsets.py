class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = []
        def dfs(nums, path):
            subsets.append(path)
            if len(nums) == 0:
                return
            
            
            for i in range(len(nums)):
                dfs(nums[i+1:], path+[nums[i]])
        
        dfs(nums, [])
        
        return subsets