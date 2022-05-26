class Solution:
    def nextGreaterElement(self, n: int) -> int:
        list_n = list(str(n))
        list_n.reverse()
        front = []
        rear = []
        for i in range(len(list_n)-1):
            rear.append(list_n[i])
            end_flg = False
            for j in range(len(rear)):
                if list_n[i+1] < rear[j] and rear[j] == min([x for x in rear if x > list_n[i+1]]):
                    front = list_n[i+1:]; front.reverse(); 
                    target_f = front.pop(); target_r = rear.pop(j)
                    front.append(target_r); rear.append(target_f)
                    rear = sorted(rear)
                    end_flg = True
                    break
            if end_flg == True: break

        if len(front) > 0:
            res = int("".join(front + rear))
            if res > 2**31 -1:
                return -1
            else:
                return res
        else:
            return -1