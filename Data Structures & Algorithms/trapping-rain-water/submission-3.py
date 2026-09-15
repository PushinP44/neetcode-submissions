class Solution:
    def trap(self, height: List[int]) -> int:
        l=0
        r=len(height)-1
        maxl=0
        maxr=0
        res=0

        while l<r:
            limit = min(height[l],height[r])
            #update maxl and maxr
            maxl=max(maxl,height[l])
            maxr=max(maxr,height[r])

            res+= maxl - height[l] + maxr - height[r]
            
            if maxl > maxr: r-=1
            else: l+=1
        return res
