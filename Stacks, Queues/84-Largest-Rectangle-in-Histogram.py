class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        stk = []
        ans = -1
        for i in range(n):
            while stk and heights[stk[-1]] >= heights[i]:
                x = heights[stk.pop()]

                if stk:
                    ans = max(ans, x * (i - stk[-1] - 1))
                else:
                    ans = max(ans, x * i)

            stk.append(i)
        while stk:
            x = heights[stk.pop()]

            if stk:
                ans = max(ans, x * (n - stk[-1] - 1))
            else:
                ans = max(ans, x * n)

        return ans
        