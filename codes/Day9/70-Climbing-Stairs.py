import math
class Solution:
    def climbStairs(self, n: int) -> int:
        # only 1
        num_ways = 1
        
        for i in range(1, (n // 2)+1):
            pattern = math.factorial(n - i) // (math.factorial(i) * math.factorial(n - (i*2)))
            num_ways = num_ways + pattern

        return num_ways