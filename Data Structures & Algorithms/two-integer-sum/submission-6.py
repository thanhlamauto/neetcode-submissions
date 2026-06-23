from collections import defaultdict

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = defaultdict(int)
        for i in range(len(nums)):
            num_dict[nums[i]] = i

        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in num_dict and num_dict[difference] != i:
                return [i, num_dict[difference]]