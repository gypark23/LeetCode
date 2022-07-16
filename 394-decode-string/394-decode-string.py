class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        
        for i in range(len(s)):
            letters = ""
            k = ""
            if s[i] != "]":
                stack.append(s[i])
            else:
                while stack[-1].isalpha():
                    letters = stack.pop() + letters
                stack.pop()
                
                while stack and stack[-1].isnumeric():
                    k = stack.pop() + k
                
                stack.append(letters * int(k))
        
        return "".join(stack)