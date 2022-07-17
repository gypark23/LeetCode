class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        dic = {}
        dic_reverse = {}
        
        for idx, prereq in enumerate(prerequisites):
            if prereq[0] in dic:
                dic[prereq[0]].append(prereq[1])
            else:
                dic[prereq[0]] = [prereq[1]]
            
            if prereq[1] in dic_reverse:
                dic_reverse[prereq[1]].append(prereq[0])
            else:
                dic_reverse[prereq[1]] = [prereq[0]]
        print(dic)
        print(dic_reverse)
        visited = set()        
        for i in range(numCourses):
            if i not in dic:
                stack = [i]
                visited.add(i)
                while stack:
                    num = stack.pop()
                    for nextcourse in dic_reverse.get(num, []):
                        if nextcourse not in visited:
                            flag = True
                            for prereq in dic[nextcourse]:
                                if prereq not in visited:
                                    flag = False
                                    break
                            if flag:
                                visited.add(nextcourse)
                                stack.append(nextcourse)
        for i in range(numCourses):
            if i not in visited:
                return False
        return True
                