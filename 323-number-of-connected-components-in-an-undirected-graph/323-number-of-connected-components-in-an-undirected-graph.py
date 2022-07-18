class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = set()
        ret = 0
        dic = {}
        
        for x, y in edges:
            if x in dic:
                dic[x].append(y)
            else:
                dic[x] = [y]
            if y in dic:
                dic[y].append(x)
            else:
                dic[y] = [x]
        
        for i in range(n):

            if i in visited:
                continue
            stack = [i]
            while stack:
                node = stack.pop()
                for neighbor in dic.get(node, []):
                    if neighbor not in visited:
                        visited.add(neighbor)
                        stack.append(neighbor)

            ret += 1
        
        return ret
            
            
        