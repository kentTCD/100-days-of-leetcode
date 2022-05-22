class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        counter = 0
        if nums[0] >= k:
            memo_dict = {0:[]}
        else:
            memo_dict = {0:[nums[0]]}
            counter += 1

        for i in range(1, len(nums)):
            if nums[i] >= k:
                memo_dict[i] = []
            elif nums[i] == 1:
                memo_dict[i] = memo_dict[i-1]
                memo_dict[i].append(nums[i])
                counter += len(memo_dict[i])
            else:
                memo_dict[i] = [num*nums[i] for num in memo_dict[i-1] if num*nums[i] < k]
                memo_dict[i].append(nums[i])
                counter += len(memo_dict[i])

        return counter