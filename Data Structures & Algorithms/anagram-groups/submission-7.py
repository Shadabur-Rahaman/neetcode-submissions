class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        g = defaultdict(list)
        for s in strs:
            keys = ''.join(sorted(s))
            g[keys].append(s)
        return list(g.values())