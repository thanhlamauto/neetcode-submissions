class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        from collections import Counter
        
        freq = Counter(tasks)

        max_freq = max(freq.values())

        max_counter = sum(1 for count in freq.values() if count == max_freq)

        return max(len(tasks), (max_freq - 1) * (n+1) + max_counter)