class TimeMap:
    from collections import defaultdict
    def __init__(self):
        self.map1 = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map1[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        n = len(self.map1[key])
        l, r = 0, n - 1
        res = ""
        while l <= r:
            mid = l + ((r-l) // 2)
            if self.map1[key][mid][0] <= timestamp:
                res = self.map1[key][mid][1]
                l = mid + 1
            else:
                r = mid - 1
        return res
        
