class MyCircularQueue:

    def __init__(self, k: int):
        self.lim = k
        self.que = deque()

    def enQueue(self, value: int) -> bool:
        if len(self.que) < self.lim:
            self.que.append(value)
            return True
        else:
            return False

    def deQueue(self) -> bool:
        if len(self.que) > 0:
            self.que.popleft()
            return True
        else:
            return False

    def Front(self) -> int:
        if len(self.que) > 0:
            return self.que[0]
        else:
            return -1

    def Rear(self) -> int:
        if len(self.que) > 0:
            return self.que[-1]
        else:
            return -1

    def isEmpty(self) -> bool:
        if len(self.que) <= 0:
            return True
        else:
            return False

    def isFull(self) -> bool:
        if len(self.que) == self.lim:
            return True
        else:
            return False


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()