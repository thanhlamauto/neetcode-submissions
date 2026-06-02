class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        left = 0
        right = n - 1
        
        while right > left:
            if numbers[right] + numbers[left] > target:
                right -= 1
            elif numbers[right] + numbers[left] < target:
                left += 1
            else:
                return [left + 1, right + 1]
            
        
