class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        heap = []
        ret = []
        for i, row in enumerate(mat):
            idx = 0
            while idx < len(row) and row[idx] == 1:
                idx += 1
            heap.append(idx + i / 1000)
        
        heapify(heap)
        while k:
            ret.append(round(heappop(heap) % 1 * 1000))
            k -= 1
        return ret