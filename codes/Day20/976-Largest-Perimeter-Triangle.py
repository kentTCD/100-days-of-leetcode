class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        while len(nums) > 2:
            if nums[-1] < nums[-2] + nums[-3]:
                return nums[-1] + nums[-2] + nums[-3]
            nums.pop()
        
        return 0