class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        arr_sum = 0
        for i in range(len(arr)):
            curr_arr = []
            for j in range(i, len(arr)):
                curr_arr.append(arr[j])
                if len(curr_arr)%2 == 1: arr_sum += sum(curr_arr)

        return arr_sum