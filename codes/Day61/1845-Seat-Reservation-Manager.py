class SeatManager:

    def __init__(self, n: int):
        self.n = 0
        self.unrsrv_count = 0
        self.unreserved = []

    def reserve(self) -> int:
        if self.unrsrv_count > 0:
            self.unrsrv_count -= 1
            return self.unreserved.pop()
        else:
            self.n += 1
            return self.n

    def unreserve(self, seatNumber: int) -> None:
        self.unrsrv_count += 1
        self.unreserved.append(seatNumber)
        self.unreserved.sort(reverse=True)