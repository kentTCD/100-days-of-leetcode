class Solution:
    ### My trial
    # def decodeString(self, s: str) -> str:
    #     stack = []
    #     brs = []
    #     for i in range(len(s)):
    #         if s[i] == "[":
    #             stack.append(i)
    #         elif s[i] == "]":
    #             brs.append((stack.pop(), i))
    #     res = ""
    #     brs.sort(key=lambda x:x[0])
    #     print(brs)
    #     for i, j in brs:
    #         res += s[i+1:j] * int(s[i-1])
    #     return res

    ### Someone's solution that helped me to understand the problem.
    def decodeString(self, s):
        stack = []; curNum = 0; curString = ''
        for c in s:
            if c == '[':
                stack.append(curString)
                stack.append(curNum)
                curString = ''
                curNum = 0
            elif c == ']':
                num = stack.pop()
                prevString = stack.pop()
                curString = prevString + num*curString
            elif c.isdigit():     # curNum*10+int(c) is helpful in keep track of more than 1 digit number
                curNum = curNum*10 + int(c)
            else:
                curString += c
        return curString