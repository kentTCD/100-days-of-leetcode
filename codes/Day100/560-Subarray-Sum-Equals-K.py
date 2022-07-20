class Solution:
    ### My solution that was stuck at TimeLimitExceeded
    # def subarraySum(self, nums: List[int], k: int) -> int:
        # sums = []
        # counts = 0
        # for i in range(len(nums)):
        #     sums.append(sums[i-1] + nums[i]) if i != 0 else sums.append(nums[0])
        #     diff = sums[i] - k 
        #     if diff == 0:
        #         counts += 1
        #     counts += sums[:i].count(diff)
        # return counts

    ### Someone's solution that tells me how effective using hashmap is
    def subarraySum(self, nums: List[int], k: int) -> int:
        ans=0
        prefsum=0
        d={0:1}

        for num in nums:
            prefsum = prefsum + num

            if prefsum-k in d:
                ans = ans + d[prefsum-k]

            if prefsum not in d:
                d[prefsum] = 1
            else:
                d[prefsum] = d[prefsum]+1

        return ans