class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        res = [-1]*len(nums)
        stack = []
        circular = nums+nums

        for i in range(len(circular)):
            while stack and nums[stack[-1]] < circular[i]:
                index = stack.pop()
                res[index] = circular[i]
            if i < len(nums):
                stack.append(i)
        return res