class Solution:
    def reverseWords(self, s: str) -> str:
        res = []
        for i in s.split():
            res.append(i[::-1])
        return " ".join(res)