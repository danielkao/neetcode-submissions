class Solution:
    def maxArea(self, heights: List[int]) -> int:
        s = 0
        e = len(heights) - 1
        area = 0
        
        while e > s:
            side = min(heights[e], heights[s])
            if (e - s) * side > area:
                area = (e - s) * side
                continue
            if side == heights[e]:
                e -= 1
                continue
            elif side == heights[s]:
                s += 1
                continue

        return area
