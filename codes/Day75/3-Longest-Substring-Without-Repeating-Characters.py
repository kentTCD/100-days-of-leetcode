class Solution:
    ### Someone's solution that I learnd from.
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxSize = l = 0
        window = {}
        for r, char in enumerate(s):
            l = window[char] + 1 if char in window and window[char] >= l else l
            window[char] = r
            maxSize = max(maxSize, r - l + 1)
        return maxSize