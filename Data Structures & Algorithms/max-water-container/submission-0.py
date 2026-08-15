class Solution:
    def maxArea(self, heights: List[int]) -> int:
        ptr1 = 0
        ptr2 = len(heights) - 1
        maxwater = 0
        while ptr2 > ptr1:
            height = min(heights[ptr1], heights[ptr2])
            width = ptr2 - ptr1
            water = height * width
            maxwater = max(water, maxwater)
            if heights[ptr1] < heights[ptr2]:
                ptr1 += 1
            else:
                ptr2 -= 1

        return maxwater
