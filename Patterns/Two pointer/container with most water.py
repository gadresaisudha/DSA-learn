class Solution:
    def maxArea(self, height: List[int]) -> int:
        start = 0
        end = len(height)-1
        maxarea = 0

        while(start<end):
            w = end - start
            h = min(height[start],height[end])
            area = w*h
            maxarea = max(area,maxarea)
            if height[start]<height[end]:
                start+=1
            else:
                end-=1
        

        return maxarea