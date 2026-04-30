class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        maxArea = 0
        
        while l < r:
            # Calculate current area
            width = r - l
            h = min(heights[l], heights[r])
            area = width * h
            maxArea = max(maxArea, area)
            
            # Move the pointer with smaller height
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        
        return maxArea


        