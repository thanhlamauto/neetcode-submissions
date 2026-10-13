class MedianFinder:

    def __init__(self):
        self.maxheap = []
        self.minheap = []

    def addNum(self, num: int) -> None:
        if self.maxheap and num >= -self.maxheap[0]:
            heapq.heappush(self.minheap, num)
        elif self.minheap and num <= self.minheap[0]:
            heapq.heappush(self.maxheap, -num)
        else:
            heapq.heappush(self.minheap, num)
        
        
        if len(self.maxheap) - len(self.minheap) > 1:
            n = -heapq.heappop(self.maxheap)
            heapq.heappush(self.minheap, n)
        elif len(self.minheap) - len(self.maxheap) > 1:
            n = heapq.heappop(self.minheap)
            heapq.heappush(self.maxheap, -n)
    

    def findMedian(self) -> float:
        if len(self.minheap) == len(self.maxheap):
            return (-self.maxheap[0] + self.minheap[0]) / 2
        elif len(self.minheap) > len(self.maxheap):
            return self.minheap[0]
        else:
            return -self.maxheap[0]
        
        