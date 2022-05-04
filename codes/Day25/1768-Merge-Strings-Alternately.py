class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        len_longer = len(word1) if len(word1) >= len(word2) else len(word2)
        merged = ""
        for i in range(len_longer):
            if i < len(word1): merged = merged + word1[i]
            if i < len(word2): merged = merged + word2[i]
        return merged