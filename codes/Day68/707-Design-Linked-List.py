class MyLinkedList:

    def __init__(self):
        self.mylnklist = []

    def get(self, index: int) -> int:
        try:
            return self.mylnklist[index]
        except IndexError:
            return -1

    def addAtHead(self, val: int) -> None:
        self.mylnklist = [val] + self.mylnklist

    def addAtTail(self, val: int) -> None:
        self.mylnklist.append(val)

    def addAtIndex(self, index: int, val: int) -> None:
        size = len(self.mylnklist)
        if index == size:
            self.mylnklist.append(val)
        elif index < size:
            self.mylnklist = self.mylnklist[:index] + [val] + self.mylnklist[index:]

    def deleteAtIndex(self, index: int) -> None:
        try:
            self.mylnklist.pop(index)
        except IndexError:
            pass

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)