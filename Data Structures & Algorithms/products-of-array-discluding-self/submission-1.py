class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = len(nums)
        res = [1]*l
        
        p = 1
        for i in range(l):
            res[i] = p
            p *= nums[i]
        
        p = 1
        for i in reversed(range(l)):
            res[i] *= p
            p *= nums[i]
        return res