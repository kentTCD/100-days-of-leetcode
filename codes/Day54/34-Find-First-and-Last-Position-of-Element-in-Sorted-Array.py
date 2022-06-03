class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        target_count = nums.count(target)
        if target_count < 1:
            return [-1, -1]
        elif target_count == 1:
            return [nums.index(target), nums.index(target)]
        elif target_count == 2:
            first_idx = nums.index(target)
            return [first_idx, first_idx+1]
        else:
            return [nums.index(target), len(nums) -1 - sorted(nums, reverse=True).index(target)]