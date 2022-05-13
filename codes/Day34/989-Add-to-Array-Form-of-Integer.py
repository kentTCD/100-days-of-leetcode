class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        sum_int = 0
        for i, n in enumerate(reversed(num)): sum_int += n * 10**i
        return str(sum_int + k)