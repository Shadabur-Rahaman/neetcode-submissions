class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = {}
        for n in nums:
            c[n] = 1 + c.get(n,0)
        arr = []
        for n,ct in c.items():
            arr.append([ct,n])
        arr.sort()
        res = []
        while len(res)<k:
            res.append(arr.pop()[1])
        return res