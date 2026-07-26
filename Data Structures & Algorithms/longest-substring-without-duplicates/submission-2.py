class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l,r,ch = 0,1,set()
        res = 0
        for r in range(len(s)):
            while s[r] in ch:
                ch.remove(s[l])
                l+=1
            ch.add(s[r])
            res = max(res,r-l+1)
        return res