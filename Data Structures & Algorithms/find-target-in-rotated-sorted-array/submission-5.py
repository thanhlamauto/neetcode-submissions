class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l, r = 0, n-1
        cut = 0
        while l < r:
            mid = l + ((r-l) // 2)
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
        cut = l
        def bin_search(l, r):
            while l <= r:
                mid = l + ((r-l) // 2)
                if nums[mid] == target:
                    return mid 
                elif nums[mid] > target:
                    r = mid - 1
                else:
                    l = mid + 1
            return -1

        res = bin_search(0, cut - 1)
        if res != -1:
            return res
        else:
            return bin_search(cut, n-1)
        
        



