class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for n in nums:
            count[n] = 1 + count.get(n,0)
        a =[]
        for n,ct in count.items():
            a.append([ct,n])
        a.sort()

        res = []
        for i in range(len(nums)):
            while len(res) < k:
                res.append(a.pop()[1])
            return res