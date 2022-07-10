class Trie:
    def __init__(self):
        self.next = {}
        self.end = False

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie = Trie()

        for word in dictionary:
            curr = trie
            for char in word:
                if char not in curr.next:
                    curr.next[char] = Trie()
                curr = curr.next[char]
            curr.end = True
        
        words = sentence.split()
        ret = ""
        for word in words:
            ret += " "
            curr = trie
            for char in word:
                if char in curr.next and curr.next[char].end:
                    ret += (char)
                    break
                else:
                    ret += char
                    if char in curr.next:
                        curr = curr.next[char]
                    else:
                        curr = Trie()
        return ret[1:]