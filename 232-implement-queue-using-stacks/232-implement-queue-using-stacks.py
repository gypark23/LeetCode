class MyQueue:

    def __init__(self):
        self.first = []
        self.second = []

    def push(self, x: int) -> None:
        self.first.append(x)

    def pop(self) -> int:
        if self.second:
            return self.second.pop()
        else:
            while self.first:
                self.second.append(self.first.pop())
            return self.pop()

    def peek(self) -> int:
        if self.second:
            return self.second[-1]
        else:
            while self.first:
                self.second.append(self.first.pop())
            return self.peek()

    def empty(self) -> bool:
        return not self.first and not self.second


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()