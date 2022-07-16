from collections import deque
class MyStack:

    def __init__(self):
        self.first = deque()
        #self.second = deque()

    def push(self, x: int) -> None:
        self.first.append(x)
        for _ in range(len(self.first) - 1):
            self.first.append(self.first.popleft())

    def pop(self) -> int:
        return self.first.popleft()
        

    def top(self) -> int:
        return self.first[0]

    def empty(self) -> bool:
        return not self.first


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()