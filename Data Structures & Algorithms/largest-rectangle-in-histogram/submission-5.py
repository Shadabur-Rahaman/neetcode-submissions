class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n,m,s = len(heights),0,[]
        for i in range(n+1):
            while s and (i==n or heights[s[-1]] >= heights[i]):
                h = heights[s.pop()]
                w = i if not s else i-s[-1]-1
                m = max(m,h*w)
            s.append(i)
        return m