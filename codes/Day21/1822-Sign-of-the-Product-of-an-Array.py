class Solution:
    def arraySign(self, nums: List[int]) -> int:
        return 1 if math.prod(nums) > 0 else -1 if math.prod(nums) < 0 else 0