class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        rev_s = s[::-1]
        cur_part = [0,0]
        res = []
        for i in range(len(s)):
            tail_idx = len(s) - 1 - rev_s.index(s[i])
            if i > cur_part[1] or i == len(s)-1:
                res.append(cur_part[1] - cur_part[0] + 1)
                if cur_part[1] == len(s)-2:
                    res.append(1)
                cur_part = [i, tail_idx]
            else:
                if tail_idx > cur_part[1]:
                    cur_part[1] = tail_idx
        return res