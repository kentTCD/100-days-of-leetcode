class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return not sorted(nums) == sorted(list(set(nums)))