class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []
        p_counter = Counter(p)
        len_p = len(p)
        window_counter = Counter(s[0:len_p-1])
        for i in range(len(s)-(len_p-1)):
            window_counter[s[i+len_p-1]] += 1
            if window_counter == p_counter:
                res.append(i)
            window_counter[s[i]] -= 1
            if window_counter[s[i]] == 0:
                del window_counter[s[i]]
        return res