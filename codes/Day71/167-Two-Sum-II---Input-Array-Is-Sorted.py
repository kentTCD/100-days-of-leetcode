class Solution:
    ### My solution
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        counter = Counter(numbers)
        for i in range(len(numbers)):
            seek = target - numbers[i]
            if counter[seek] != 0:
                return [i+1, i + 1 + numbers[i+1:].index(seek)+1]

    ### Someones's solution that helped me learn about two-pointers
    def twoSum(self, numbers, target):
            """
            :type numbers: List[int]
            :type target: int
            :rtype: List[int]
            """
            l = 0
            r = len(numbers) - 1
            while l < r:
                if numbers[l] + numbers[r] == target:
                    return [l+1, r+1]
                elif numbers[l] + numbers[r] > target:
                    r -= 1
                else:
                    l += 1
            return