class MinStack:

    def __init__(self):
        self.nums = []
        self.mins = []

    def push(self, val: int) -> None:
        self.nums.append(val)
        if not self.mins or val <= self.mins[-1]:
            self.mins.append(val)
    def pop(self) -> None:
        val = self.nums.pop()
        if val == self.mins[-1]:
            self.mins.pop()

    def top(self) -> int:
        return self.nums[-1]

    def getMin(self) -> int:
        return self.mins[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()