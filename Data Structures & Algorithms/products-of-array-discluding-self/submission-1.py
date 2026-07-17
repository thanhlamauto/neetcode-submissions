class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = len(nums)
        left = []
        right = [0] * l
        res = []
        for i in range(l):
            if i == 0:
                left.append(nums[i])
                right[l-1] = nums[l-1]
            else:
                left.append(nums[i]*left[i-1])
                right[l - 1 - i] = nums[l - 1 - i]*right[l-i]
        
        for j in range(l):
            if j == 0:
                res.append(right[1])
            elif j == l-1:
                res.append(left[l-2])
            else:
                res.append(right[j+1] * left[j-1])
        print(left)
        print(right)
        return res