class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        pairs = sorted(zip(position, speed), reverse=True)
        position, speed = map(list, zip(*pairs))
        count = 0
        stack = []

        for i in range(n):
            if not stack:
                stack.append(i)
                count += 1
            elif ((target - position[i]) / speed[i]) > ((target - position[stack[-1]]) / speed[stack[-1]]):
                stack.clear()
                stack.append(i)
                count += 1
        return count

