class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        cur_max = cur_min = res = nums[0]

        for num in nums[1:]:
            if num < 0:
                cur_max, cur_min = cur_min, cur_max
            
            cur_max = max(num, cur_max*num)
            cur_min = min(num, cur_min*num)

            res = max(res, cur_max)
        return res



