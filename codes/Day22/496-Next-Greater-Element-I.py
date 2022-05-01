class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        for num in nums1:
            n2_index = nums2.index(num)
            if n2_index == len(nums2)-1:
                res.append(-1)
            else:
                for i in range(n2_index+1, len(nums2)):
                    if nums2[i] > num:
                        res.append(nums2[i])
                        break
                    if i == len(nums2)-1: res.append(-1)

        return res