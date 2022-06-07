class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(len(nums)):
            if nums[i] != i and i <= len(nums)-1:
                return nums[i] - 1
            elif nums[i] == i and i == len(nums)-1:
                return nums[i] + 1