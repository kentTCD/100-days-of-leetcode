class Solution:
    ### Mine almost done
#     def lengthOfLIS(self, nums: List[int]) -> int:
#         self.nums = nums
#         return self.counter(0)
        
#     def counter(self, first_id: int):
#         first, second = self.nums[first_id], None
#         count = count_2 = 1
#         isRecursed = False
#         for i in range(first_id + 1, len(self.nums)):
#             if second is None:
#                 if first < self.nums[i]:
#                     second = self.nums[i]
#                     count += 1
#                 else:
#                     first = self.nums[i]
#             else:
#                 if second < self.nums[i]:
#                     first = second
#                     second = self.nums[i]
#                     count += 1
#                 else:
#                     if first < self.nums[i]:
#                         second = self.nums[i]
#                     elif first > self.nums[i] and (not isRecursed):
#                         count_2 = self.counter(i)
#                         isRecursed = True
#         return max(count, count_2)

    ### Someone's solution that I learned from
    def lengthOfLIS(self, nums):
        sub = []
        for val in nums:
            pos , sub_len = 0, len(sub)
            while(pos <= sub_len):    # update the element to the correct position of the sub.
                if pos == sub_len:
                    sub.append(val)
                    break
                elif val <= sub[pos]:
                    sub[pos] = val
                    break
                else:
                    pos += 1
        
        return len(sub)