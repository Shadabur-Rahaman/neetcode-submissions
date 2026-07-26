class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        p = [[p,s] for p,s in zip(position,speed)]
        p.sort(reverse = True)
        f = 1
        pt = (target-p[0][0])/p[0][1]
        for i in range(1,len(p)):
            c = p[i]
            ct = (target-c[0])/c[1]
            if ct>pt:
                f+=1
                pt = ct
        return f