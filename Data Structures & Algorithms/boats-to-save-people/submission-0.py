class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        n = len(people)
        left = 0
        right = n-1
        count = 0

        while left < right and people[right] == limit:
            right -= 1
            count += 1
            
            
        
        while left <= right:
            if people[left] + people[right] > limit:
                count += 1
                right -= 1
            elif people[left] + people[right] <= limit:
                count += 1
                left += 1
                right -= 1
        return count 

        1, 2, 2, 3, 3
        