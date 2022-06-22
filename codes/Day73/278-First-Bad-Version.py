# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        mini, maxi = 1, n
        while mini != maxi:
            cent = mini + (maxi - mini)//2
            if isBadVersion(cent):
                maxi = cent - 1 if mini != cent and isBadVersion(cent-1) else maxi - 1
            else:
                mini = cent + 1
        return mini