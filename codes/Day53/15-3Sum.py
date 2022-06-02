class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        counter_nums = Counter(nums)
        counter_nums_keys = list(counter_nums.keys())
        for i in range(len(counter_nums)):
            for j in range(i, len(counter_nums)):
                if i == j and counter_nums[counter_nums_keys[i]] < 2:
                    continue
                num1, num2 = counter_nums_keys[i], counter_nums_keys[j]
                num3 = (num1 + num2) * -1
                dup_count = 2 if num1 == num3 and num2 == num3 else 1 if (num1 == num3 or num2 == num3) and num1 != num2 else 0

                if num3 in counter_nums.keys():
                    if counter_nums[num3] > dup_count:
                        res.append(sorted([num1, num2, num3]))

        return list(map(list, set(map(tuple, res))))