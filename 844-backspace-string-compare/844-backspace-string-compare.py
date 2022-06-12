class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack_s = [0] * 200
        stack_t = [0] * 200
        idx_s, idx_t = 0, 0
        
        for char in s:
            if(char == '#'):
                idx_s -= 1
                idx_s = max(0, idx_s)
                stack_s[idx_s] = 0
            else:
                stack_s[idx_s] = char
                idx_s += 1
        
        for char in t:
            if(char == '#'):
                idx_t -= 1
                idx_t = max(0, idx_t)
                stack_t[idx_t] = 0
            else:
                stack_t[idx_t] = char
                idx_t += 1
                

        return stack_s == stack_t