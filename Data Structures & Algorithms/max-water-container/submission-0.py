class Solution:
    def maxArea(self, heights: List[int]) -> int:
        ans = []
        for i in range(len(heights)):
            for j in range(i+1,len(heights)):
                min_area = min(heights[i],heights[j])
                ans.append(min_area * (j-i))
        return max(ans)