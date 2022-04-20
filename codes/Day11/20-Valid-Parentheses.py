class Solution:
    def isValid(self, s: str) -> bool:
        len_s = len(s)
        if len_s % 2 == 1: return False
        
        left_brckts = ["(", "{", "["]
        right_brckts = [")", "}", "]"]
        a_team = ["(", ")"]
        b_team = ["{", "}"]
        c_team = ["[", "]"]
        
        if s[0] not in left_brckts or s[-1] not in right_brckts: return False
        
        char_list = []
        for i in range(len_s):
            char = s[i]
            if len(char_list) == 0 and (char not in left_brckts):
                return False
            else:
                if char in right_brckts:
                    last = char_list.pop()
                    if not((char in a_team and last in a_team) or (char in b_team and last in b_team) or (char in c_team and last in c_team)): return False
                else: char_list.append(char)
        if len(char_list) != 0: return False
        
        return True