class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        g = defaultdict(list)
        for i in strs:
            count = [0] * 26
            for c in i:
                count[ord(c)-ord('a')] += 1
            g[tuple(count)].append(i)
        return list(g.values())

            