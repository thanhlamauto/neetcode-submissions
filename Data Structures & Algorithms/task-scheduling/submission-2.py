class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        from collections import Counter, deque
        freq = Counter(tasks)

        maxheap = [-count for count in freq.values()]
        heapq.heapify(maxheap)
        print(maxheap)

        queue = deque()
        
        time = 0

        while queue or maxheap:
            time += 1

            if queue and queue[0][1] <= time:
                count, avail = queue.popleft()
                heapq.heappush(maxheap, count)

            if maxheap:
                count = heapq.heappop(maxheap)

                count += 1

                if count < 0:
                    queue.append((count, time + n + 1))
        
        return time 


