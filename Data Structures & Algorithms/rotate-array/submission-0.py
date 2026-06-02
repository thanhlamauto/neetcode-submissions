class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        old_nums = nums.copy()
        k = k % n

        for i in range(n):
            nums[i] = old_nums[i - k]
        

        