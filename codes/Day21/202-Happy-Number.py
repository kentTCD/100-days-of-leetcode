class Solution:
    def isHappy(self, n: int) -> bool:
        results = []
        result = n
        while result not in results:
            results.append(result)
            tmp = 0
            for num in str(result):
                tmp += int(num)*int(num)
            result = tmp
            if result == 1: return True
        
        return False
            