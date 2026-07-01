class Solution:
    from collections import defaultdict
    import heapq
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # count = defaultdict(int)
        # for num in nums:
        #     count[num] += 1
        
        # heap = []
        # for key, value in count.items():
        #     heapq.heappush(heap, (value, key))
        #     if len(heap) > k:
        #         heapq.heappop(heap)
        
        # res = []
        # for i in range(k):
        #     res.append(heapq.heappop(heap)[1])
        # return res

        n = len(nums)
        freq = [[] for i in range(n + 1)]

        count = defaultdict(int)
        for num in nums:
            count[num] += 1
        
        for key, value in count.items():
            freq[value].append(key)

        res = []
        for i in range(n, 0, -1):
            for item in freq[i]:
                res.append(item)
                k -= 1
                if k < 1:
                    break
            if k < 1:
                break
        return res
