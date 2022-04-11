class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        rtn_list = []
        for i in range(1, n+1):
            if i % 3 == 0 and i % 5 == 0:
                rtn_list.append("FizzBuzz")
            elif i % 3 == 0:
                rtn_list.append("Fizz")
            elif i % 5 == 0:
                rtn_list.append("Buzz")
            else:
                rtn_list.append(str(i))

        return rtn_list