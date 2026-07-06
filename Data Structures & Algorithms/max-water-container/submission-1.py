class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_height = 0
        i,j = 0, len(heights)-1
        while i<j:
            curr = (j-i) * (min(heights[i], heights[j]))
            max_height = max(max_height,curr)
            if heights[i] < heights[j]:
                i+=1
            else:
                j-=1
        return max_height