class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        len_nums = len(nums)
        if k >= len_nums:
            k -= len_nums * (k // len_nums)

        for i in range(k):
            tail = nums.pop()
            nums.insert(0,tail)