class Solution:
    def maxArea(self, height: List[int]) -> int:
        area=0
        left=0
        right=len(height)-1
        while(left<right):
            water_level=min(height[left],height[right])
            b=right-left
            a=water_level*b
            area=max(area,a)
            if(height[left]<height[right]):
                left+=1
            else:
                right-=1
        return area
        