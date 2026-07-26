class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        for i in range(len(s)):
            count,m = {},0
            for j in range(i,len(s)):
                count[s[j]] = 1 + count.get(s[j],0)
                m = max(m,count[s[j]])
                if (j-i+1) - m <= k:
                    res = max(res,j-i+1)
        return res