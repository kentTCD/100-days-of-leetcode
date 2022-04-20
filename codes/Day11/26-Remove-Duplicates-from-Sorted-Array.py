class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        singles = sorted(list(set(nums)))
        for i in range(len(singles)):
            nums[i] = singles[i]
        
        return len(singles)