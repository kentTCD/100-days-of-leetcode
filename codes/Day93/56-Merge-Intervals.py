class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        i = 0
        for intvl in sorted(intervals, key=lambda x: x[0]):
            if i > 0 and res[-1][1] >= intvl[0]:
                res[-1][1] = max(res[-1][1], intvl[1])
            else:
                res.append(intvl)
            i += 1
        return res