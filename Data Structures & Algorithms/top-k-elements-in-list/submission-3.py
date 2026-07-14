class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = {}
        for n in nums:
            c[n] = 1 + c.get(n,0)
        a = []
        for n,i in c.items():
            a.append([i,n])
        a.sort()
        res = []
        for n in nums:
            while len(res) < k:
                res.append(a.pop()[1])
        return res