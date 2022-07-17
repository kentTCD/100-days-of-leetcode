class Solution:
    def countSubstrings(self, s: str) -> int:
        ### My solution that couldn't solve it
        # len_s = len(s)
        # if len_s == 1:
        #     return 1
        # sub_lengs = []
        # for i in range(len_s):
        #     if i == 0:
        #         sub_lengs.append(1)
        #         continue
        #     if s[i-1] == s[i]:
        #         sub_lengs[-1] += 1
        #     else:
        #         sub_lengs.append(1)
        # num = 0
        # for sub_len in sub_lengs:
        #     num += sum([i for i in range(1, sub_len+1)])
        # return num

        ### The solution that I admired on YouTube
        res = 0
        for i in range(len(s)):
            res += self.countPali(s, i , i)
            res += self.countPali(s, i, i + 1)
        return res

    def countPali(self, s, l, r):
        res = 0
        while l >= 0 and r < len(s) and s[l] == s[r]:
            res += 1
            l -= 1
            r += 1
        return res