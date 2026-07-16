class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        f = [[]for i in range(len(nums)+1)]
        for n in nums:
            count[n] = 1 + count.get(n,0)

        for i,ct in count.items():
            f[ct].append(i)

        res = []
        for i in range(len(f)-1,0,-1):
            for n in f[i]:
                res.append(n)
            while len(res) == k:
                return res
            