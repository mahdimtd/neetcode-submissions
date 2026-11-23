class Solution:
    def maxArea(self, height: list[int]) -> int:
        x,y=0,len(height)-1
        best = 0
        while x < y:
            area = (y - x )* min(height[x],height[y])
            best = max(best,area)
            if height[x] < height[y]:
                x +=1
            else:
                y -=1
        return best