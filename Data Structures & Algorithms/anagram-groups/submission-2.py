class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        g = defaultdict(list)
        for s in strs:
            k = ''.join(sorted(s))
            g[k].append(s)
        return list(g.values())