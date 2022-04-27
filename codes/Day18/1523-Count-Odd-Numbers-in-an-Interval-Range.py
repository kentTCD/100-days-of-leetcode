class Solution:
    def countOdds(self, low: int, high: int) -> int:
        odd_count = (high-low)//2 if low%2 == 0 and high%2 == 0 else (high-low)//2 +1
        return odd_count