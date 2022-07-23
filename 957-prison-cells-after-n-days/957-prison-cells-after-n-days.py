class Solution:
    def prisonAfterNDays(self, cells: List[int], n: int) -> List[int]:
        temp = cells[:]
        visited = {}
        i = 0
        while i < n:
            temp = [0] * 8
            for j in range(1, 7):
                temp[j] = 1 if cells[j - 1] == cells[j + 1] else 0
            cells, temp = temp, cells
            
            if tuple(cells) in visited:
                cycle = visited[tuple(cells)] - i
                return self.prisonAfterNDays(cells[:], (n - 1) % abs(cycle))
            else:
                visited[tuple(cells)] = i
            i += 1
        return cells