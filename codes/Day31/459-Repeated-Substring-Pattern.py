class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        devider = 2
        while len(s) / devider >= 1:
            if len(s) % devider == 0:
                subst = s[:len(s)//devider]
                if s.count(subst) == devider: return True
            devider += 1
        return False