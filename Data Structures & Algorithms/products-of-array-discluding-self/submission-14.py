class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1]*n
        p=1
        for i in range(n):
            res[i] = p
            p *= nums[i]
        p = 1
        for i in reversed(range(n)):
            res[i] *= p 
            p *= nums[i]
        return res