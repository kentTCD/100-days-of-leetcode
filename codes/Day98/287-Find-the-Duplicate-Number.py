class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # nums_count = len(nums)
        # largest = sorted(nums)[-1]
        # diff = sum(nums) - sum(range(1, largest+1))
        # return diff // (nums_count - largest)
        for i, num in enumerate(sorted(nums)):
            if i == 0:
                prev_num = num
            else:
                if num == prev_num:
                    return num
                else:
                    prev_num = num