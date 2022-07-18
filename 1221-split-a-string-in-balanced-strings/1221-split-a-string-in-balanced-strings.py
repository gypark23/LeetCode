class Solution:
    def balancedStringSplit(self, s: str) -> int:
        ret = 0
        num_r, num_l = 0, 0
        for char in s:
            if char == "R":
                num_r += 1
            else:
                num_l += 1
            
            if num_r == num_l:
                num_r, num_l = 0, 0
                ret += 1
        
        return ret