class MapSum:

    def __init__(self):
        self.next = {}
        self.val = 0
        self.keys = {}

    def insert(self, key: str, val: int) -> None:
        curr = self
        delta = val - self.keys.get(key, 0)
        self.keys[key] = val
        for char in key:
            if char not in curr.next:
                curr.next[char] = MapSum()
            curr.val += delta
            curr = curr.next[char]
        curr.val += delta
    def sum(self, prefix: str) -> int:
        curr = self
        for char in prefix:
            if char not in curr.next:
                return 0
            curr = curr.next[char]
        return curr.val


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)