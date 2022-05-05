class Solution:
    def toLowerCase(self, s: str) -> str:
        lower_s = ""
        for char in s:
            lower_s = lower_s + chr(ord(char)+32) if ord(char) >= 65 and ord(char) <= 90 else lower_s + char
        return lower_s