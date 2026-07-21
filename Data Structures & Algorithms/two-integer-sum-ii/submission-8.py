class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l,r,summ = 0,len(numbers)-1,0
        while l<r:
            summ = numbers[l] + numbers[r]
            if summ == target:
                return [l+1,r+1]
            elif summ < target:
                l+=1
            else:
                r-=1
        

            