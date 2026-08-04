class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for n in nums:
            count[n] = 1 + count.get(n,0)
        a = []
        for i,n in count.items():
            a.append([n,i])
        a.sort()
        res = []
        while len(res)<k:
            res.append(a.pop()[1])
        return res