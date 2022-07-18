class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        arr = [[0] * len(words) for i in range(26)]
        
        for idx, word in enumerate(words):
            for char in word:
                arr[ord(char) - ord('a')][idx] += 1
        
        ret = []
        for i in range(26):
            while all(arr[i]):
                ret.append(chr(i + ord('a')))
                for j in range(len(arr[i])):
                    arr[i][j] -= 1
        
        return ret
        
            