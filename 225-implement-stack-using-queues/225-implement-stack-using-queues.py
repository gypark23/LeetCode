from collections import deque
class MyStack:

    def __init__(self):
        self.first = deque()
        self.second = deque()
        self._top = None
        
    def push(self, x: int) -> None:
        self.first.append(x)
        self._top = x

    def pop(self) -> int:
        while len(self.first) > 1:
            self._top = self.first.popleft()
            self.second.append(self._top)
        
        self.first, self.second = self.second, self.first
        return self.second.popleft()

    def top(self) -> int:
        return self._top

    def empty(self) -> bool:
        return not self.first and not self.second


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()