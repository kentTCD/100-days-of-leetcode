class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        way = 'increase' if nums[-1] > nums[0] else 'decrease' if nums[-1] < nums[0] else 'stay'
        for i in range(1, len(nums)):
            if way == 'increase':
                if nums[i] < nums[i-1]: return False
            elif way == 'decrease':
                if nums[i] > nums[i-1]: return False
            else:
                if nums[i] != nums[i-1]: return False
        return True