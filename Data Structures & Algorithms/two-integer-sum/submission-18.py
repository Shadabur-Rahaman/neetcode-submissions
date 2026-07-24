class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i,n in enumerate(nums):
            summ = target - nums[i]
            if summ in seen:
                return[seen[summ],i]
            seen[n] = i
        