class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        ret = [0] * len(temperatures)
        
        for curr_date, curr_temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < curr_temp:
                prev_date = stack.pop()
                ret[prev_date] = curr_date - prev_date
            stack.append(curr_date)
        
        return ret
            