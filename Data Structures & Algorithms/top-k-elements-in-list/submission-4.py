class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = {}
        fq = [[] for i in range(len(nums)+1)]
        for n in nums:
            c[n] = 1 + c.get(n,0)
        for n,i in c.items():
            fq[i].append(n)
        res = []
        for i in range(len(fq)-1,0,-1):
            for n in fq[i]:
                res.append(n)
                if len(res) == k:
                    return res