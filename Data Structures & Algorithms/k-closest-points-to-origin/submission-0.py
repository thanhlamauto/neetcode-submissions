class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        from math import sqrt
        from collections import defaultdict


        hash_map = defaultdict(list)
        for x,y in points:
            distance = sqrt(x**2 + y**2)
            hash_map[distance].append([x,y])
        distances = [sqrt(x**2 + y**2) for (x,y) in points]

        heapq.heapify(distances) 

        res = []
        while len(res) < k:
            dist = heapq.heappop(distances)
            coor = hash_map[dist]
            res.append(coor.pop())
        
        return res