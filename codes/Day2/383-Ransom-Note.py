class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        rnsm_list = list(ransomNote)
        mgzn_list = list(magazine)
        for rnsm in rnsm_list:
            i = 0
            if not rnsm in mgzn_list:
                return False
            for mgzn in mgzn_list:
                if rnsm == mgzn:
                    mgzn_list.pop(i)
                    break
                i = i + 1

        return True