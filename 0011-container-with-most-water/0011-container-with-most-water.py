class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxi = 0
        i = 0
        j = len(height) - 1

        while i < j:
            width = j - i
            h = min(height[i],height[j])

            area = width * h

            if area > maxi:
                maxi = area
            
            if height[i] < height[j]:
                i = i + 1
            else:
                j = j - 1
        
        return maxi      