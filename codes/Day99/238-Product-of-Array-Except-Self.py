class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        counts_zero = nums.count(0)
        if counts_zero == 1:
            counts_nums = len(nums)
            zero_idx = nums.index(0)
            nums.pop(zero_idx)
            ans = [0] * counts_nums
            ans[zero_idx] = math.prod(nums)
            return ans
        elif counts_zero > 1:
            counts_nums = len(nums)
            return [0] * counts_nums
        else:
            all_prod = math.prod(nums)
            return [all_prod // num for num in nums]