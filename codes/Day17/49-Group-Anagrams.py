class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        m = dict()
        for s in strs:
            sorted_s = ''.join(sorted(s))
            m[sorted_s] = m.get(sorted_s, [])
            m[sorted_s] += [s]
        return m.values()