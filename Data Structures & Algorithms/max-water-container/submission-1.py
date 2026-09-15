class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l=0
        r=len(heights)-1
        area = 0

        while l < r: 
            height = min(heights[l],heights[r])
            num = r-l
            area = max(area,height*num)
            if heights[l]>heights[r]: r-=1
            else: l+=1
        
        return area
