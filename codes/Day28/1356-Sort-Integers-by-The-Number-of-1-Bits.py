class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        arr.sort(reverse=True)
        rtn_arr = [arr[0]]
        for i in range(1, len(arr)):
            bin_num = bin(arr[i])[2:]
            counter_a = 0
            for b_n in bin_num:
                counter_a += int(b_n)
            for j in range(len(rtn_arr)):
                bin_num = bin(rtn_arr[j])[2:]
                counter_b = 0
                for b_n in bin_num:
                    counter_b += int(b_n)
                if counter_a <= counter_b:
                    rtn_arr = rtn_arr[:j] + [arr[i]] + rtn_arr[j:]
                    break
                if j == len(rtn_arr)-1: rtn_arr.append(arr[i])
        return rtn_arr