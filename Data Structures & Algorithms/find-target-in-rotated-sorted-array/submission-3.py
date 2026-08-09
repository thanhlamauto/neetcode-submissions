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
        def bin_search(target, nums, start):
            n = len(nums)
            if n < 1:
                return -1
            l, r = 0, n-1
            while l <= r:
                mid = l + ((r-l) // 2)
                if nums[mid] == target:
                    return mid + start
                elif nums[mid] > target:
                    r = mid - 1
                else:
                    l = mid + 1
            return -1

        print(cut)
        print(bin_search(target, nums[0:cut], 0))
        print(bin_search(target, nums[cut:n], cut))
        return max(bin_search(target, nums[0:cut], 0),bin_search(target, nums[cut:n], cut))



