class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for n in nums:
            count[n] = 1 + count.get(n,0)
        arr = []
        for i,ct in count.items():
            arr.append([ct,i])
        arr.sort()
        res = []
        for i in range(len(nums)):
            while len(res) < k:
                res.append(arr.pop()[1])
            return res