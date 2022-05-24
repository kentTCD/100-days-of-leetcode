class Solution:
    def smallestRangeII(self, nums: List[int], k: int) -> int:
        nums.sort()
        mn, mx = nums[0], nums[-1]
        res = mx - mn
        for i in range(len(nums)-1):
            if nums[i] < nums[i+1]:
                mx = max(nums[-1] - k, nums[i]   + k)
                mn = min(nums[0]  + k, nums[i+1] - k)
                res = min(res, mx - mn)

        return res