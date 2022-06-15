import random

class RandomizedSet:

    def __init__(self):
        self.map = {}

    def insert(self, val: int) -> bool:
        if self.map.get(val):
            return False
        else:
            self.map[val] = True
            return True

    def remove(self, val: int) -> bool:
        if self.map.get(val):
            self.map.pop(val)
            return True
        else:
            return False

    def getRandom(self) -> int:
        return random.choice(list(self.map.keys()))


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()