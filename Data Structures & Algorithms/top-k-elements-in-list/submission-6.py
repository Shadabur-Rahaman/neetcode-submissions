class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        fq = [[]for i in range(len(nums)+1)]
        for n in nums:
            count[n] = 1 + count.get(n,0)
        for n,ct in count.items():
            fq[ct].append(n)
        res = []
        for i in range(len(fq)-1,0,-1):
            for n in fq[i]:
                res.append(n)
                if len(res)==k:
                    return res