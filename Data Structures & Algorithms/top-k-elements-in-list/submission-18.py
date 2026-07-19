class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = {}
        f = [[]for i in range(len(nums)+1)]
        for n in nums:
            c[n] = 1 + c.get(n,0)
        for n,ct in c.items():
            f[ct].append(n)
        res = []
        for i in range(len(f)-1,0,-1):
            for n in f[i]:
                res.append(n)
                while len(res) == k:
                    return res