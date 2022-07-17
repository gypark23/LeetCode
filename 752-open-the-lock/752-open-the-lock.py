from collections import deque
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends = set(deadends)
        visited = set()
        visited.add('0000')
        queue = deque()
        queue.append('0000')
        ret = 0
        while queue:
            size = len(queue)
            for _ in range(size):
                code = queue.popleft()
                if code == target:
                    return ret
                if code not in deadends:
                    for idx in range(len(code)):
                        if code[idx] == '0':
                            new_code = list(code[:])
                            new_code[idx] = '9'
                            new_code = ''.join(new_code)
                            if new_code not in visited and new_code not in deadends:
                                visited.add(new_code)
                                queue.append(new_code)
                            new_code = list(code[:])
                            new_code[idx] = '1'
                            new_code = ''.join(new_code)
                            if new_code not in visited and new_code not in deadends:
                                visited.add(new_code)
                                queue.append(new_code)
                        else:
                            new_code = list(code[:])
                            new_code[idx] = chr(ord(code[idx]) + 1) if code[idx] != '9' else '0'
                            new_code = ''.join(new_code)
                            if new_code not in visited and new_code not in deadends:
                                visited.add(new_code)
                                queue.append(new_code)
                            new_code = list(code[:])
                            
                            new_code[idx] = chr(ord(code[idx]) - 1)
                            new_code = ''.join(new_code)
                            if new_code not in visited and new_code not in deadends:
                                visited.add(new_code)
                                queue.append(new_code)
            ret += 1
        
        return -1
            