class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # s.reverse()
        for i in range(len(s)-1):
            end = s.pop()
            s.insert(i, end)
