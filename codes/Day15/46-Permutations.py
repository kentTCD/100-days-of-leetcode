class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        rtn_list = []
        def dfs(nums, path):
            if len(nums) == 0:
                return rtn_list.append(path)
            
            for i in range(len(nums)):
                copy_nums = nums.copy()
                add_num = copy_nums.pop(i)
                dfs(copy_nums, path+[add_num])
                
        dfs(nums, [])
        return rtn_list