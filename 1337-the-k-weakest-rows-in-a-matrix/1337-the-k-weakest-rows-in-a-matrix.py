class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        def binarySearch(i):
            low, high = 0, len(mat[i])
            while low < high:
                mid = (low + high) // 2
                if mat[i][mid] == 1:
                    low = mid + 1
                else:
                    high = mid
            return low
            
        heap = []
        for i, row in enumerate(mat):
            item = (-binarySearch(i), -i)
            print(item)
            heappush(heap, item)
            while(len(heap) > k):
                heappop(heap)
        
        ret = []
        print(heap)
        while heap:
            a, b = heappop(heap)
            ret.append(-b)
            
        return ret[::-1]
            