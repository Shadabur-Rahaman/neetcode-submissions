class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        g = defaultdict(list)
        for s in strs:
            key = ''.join(sorted(s))
            g[key].append(s)
        return list(g.values())