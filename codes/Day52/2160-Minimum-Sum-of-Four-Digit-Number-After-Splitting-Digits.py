class Solution:
    def minimumSum(self, num: int) -> int:
        split = sorted(list(str(num)))
        return (int(split[0])*10 + int(split[2])) + (int(split[1])*10 + int(split[3]))