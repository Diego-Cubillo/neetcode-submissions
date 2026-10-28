class Solution:
    def maxArea(self, heights: List[int]) -> int:
        lIndex = 0
        rIndex = len(heights) - 1
        maxArea = 0

        while lIndex < rIndex:
            area = (rIndex - lIndex) * min(heights[rIndex], heights[lIndex])
            maxArea = max(area, maxArea)

            if heights[rIndex] < heights[lIndex]:
                rIndex -= 1
            else:
                lIndex += 1

        return maxArea
        


"""
h(xl+n) * (xr - xl - n) > maxArea

h(xl+n) > (h(xl) * (xr - xl)) / (xr - xl - n)
h(xl+n) > currArea / (xr - xl - n)
"""