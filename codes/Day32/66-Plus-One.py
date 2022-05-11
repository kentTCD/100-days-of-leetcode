class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = 0
        i = 0
        for digit in reversed(digits):
            num += digit*(10**i)
            i += 1
        return list(str(num+1))