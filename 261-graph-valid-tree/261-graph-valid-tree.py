class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1: return False
        visited = set()
        stack = [0]
        visited.add(0)
        dic = {}
        parent = {}
        for idx, edge in enumerate(edges):
            if edge[0] not in dic:
                dic[edge[0]] = [edge[1]]
            else:
                dic[edge[0]].append(edge[1])
            if edge[1] not in dic:
                dic[edge[1]] = [edge[0]]
            else:
                dic[edge[1]].append(edge[0])
                
        while stack:
            node = stack.pop()
            for leaf in dic.get(node, []):
                if parent.get(node, 9999) == leaf:
                    continue
                if leaf in visited:
                    return False
                parent[leaf] = node
                stack.append(leaf)
                visited.add(leaf)
        
        for i in range(n):
            if i not in visited:
                return False
        
        return True