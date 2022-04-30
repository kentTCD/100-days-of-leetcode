class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2: return True
        tmp = s2
        dif_indexes = []
        for i in range(len(s1)):
            if s1[i] not in tmp: return False
            if s1[i] != s2[i]:
                dif_indexes.append(i)
                if len(dif_indexes) > 2: return False
            tmp = tmp.replace(s1[i], '', 1)
        if s1[dif_indexes[0]] != s2[dif_indexes[1]] or s1[dif_indexes[1]] != s2[dif_indexes[0]]: return False
        return True