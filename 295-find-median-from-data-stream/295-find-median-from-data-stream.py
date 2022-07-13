class MedianFinder:

    def __init__(self):
        self.low = []
        self.high = []

    def addNum(self, num: int) -> None:
        if len(self.low) == len(self.high):
            if len(self.low) == 0 or num < self.high[0]:
                heappush(self.low, -num)
            else:
                heappush(self.low, -heappop(self.high))
                heappush(self.high, num)
        else:
            if num > -self.low[0]:
                heappush(self.high, num)
            else:
                heappush(self.high, -heappop(self.low))
                heappush(self.low, -num)
                

    def findMedian(self) -> float:
        if len(self.low) == len(self.high):
            return (self.high[0] - self.low[0]) / 2
        else:
            return -self.low[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()