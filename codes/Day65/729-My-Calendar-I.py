class MyCalendar:

    def __init__(self):
        self.bookings = []

    def book(self, start: int, end: int) -> bool:
        for bks in self.bookings:
            if (start >= bks[0] and start < bks[1]) or (end > bks[0] and end <= bks[1]):
                return False
            if (bks[0] >= start and bks[0] < end) or (bks[1] > start and bks[1] <= end):
                return False
        self.bookings.append([start, end])
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)