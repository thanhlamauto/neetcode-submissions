class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = [-x for x in stones]
        heapq.heapify(max_heap)

        while len(max_heap) >= 2:
            stone1 = -heapq.heappop(max_heap)
            stone2 = -heapq.heappop(max_heap)
            new_stone = abs(stone1 - stone2)
            if new_stone > 0:
                heapq.heappush(max_heap, -new_stone)
        
        return -max_heap[0] if len(max_heap) >= 1 else 0