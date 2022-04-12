class Solution:
    def numberOfSteps(self, num: int) -> int:
        i = 0
        result = num
        while result > 0:
            if result % 2 == 0:
                result = result / 2
            else:
                result = result - 1
            i = i + 1

        return i