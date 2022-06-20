class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeroes = []
        zero_count = 0
        for i in range(len(nums)):
            if nums[i - zero_count] == 0:
                zeroes.append(nums.pop(i - zero_count))
                zero_count += 1
        nums.extend(zeroes)