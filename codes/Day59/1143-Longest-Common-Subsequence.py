class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        N = len(text1)
        M = len(text2)
        
        dptable = [[0]*(N+1) for _ in range(M+1)]
    
        for row in range(1, M+1):
            for col in range(1,N+1):
                
                dptable[row][col] = max(dptable[row-1][col-1]+ (1 if text1[col-1] == text2[row-1] else 0), 
                                        dptable[row][col-1], 
                                        dptable[row-1][col]
                                       )
                
        return dptable[-1][-1]