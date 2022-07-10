class Trie():
    def __init__(self):
        self.next = {}
        self.end = False
    
class WordDictionary:

    def __init__(self):
        self.trie = Trie()

    def addWord(self, word: str) -> None:
        curr = self.trie
        for char in word:
            if char not in curr.next:
                curr.next[char] =  Trie()
            curr = curr.next[char]
        curr.end = True

    def search(self, word: str) -> bool:
        def _search(t, w):
            curr = t
            idx = 0
            for char in w:
                if char == ".":
                    for key in curr.next.keys():
                        temp = (w[idx + 1:] if idx < len(w) else "")
                        temp_curr = curr.next[key]
                        if _search(temp_curr, temp):
                            return True
                    return False
                if char not in curr.next:
                    return False
                curr = curr.next[char]
                idx += 1
            
            return curr.end
        
        return _search(self.trie, word)
    
    

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)