class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        res=[]
		
        def dfs(nums,target,path):
            if target==0:
                res.append(path)
                return
            if target<0:
                return
            
            for i in range(len(nums)):
                dfs(nums[i:],target-nums[i],path+[nums[i]])
        
        dfs(nums,target,[])
        return res