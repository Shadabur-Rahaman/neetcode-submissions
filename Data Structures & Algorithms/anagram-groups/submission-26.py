class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        g = defaultdict(list)
        for s in strs:
            res = [0] * 26
            for c in s:
                res[ord('a')-ord(c)] +=1
            g[tuple(res)].append(s)
        return list(g.values())