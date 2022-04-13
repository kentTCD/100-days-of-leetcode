class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for key, val in enumerate(nums):
            if hashmap.get(val) is None:
                hashmap[target - val] = key
            else:
                return [hashmap[val], key]