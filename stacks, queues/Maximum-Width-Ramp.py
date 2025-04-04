class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        s = []
        res = 0
        for i, a in enumerate(nums):
            if not s or nums[s[-1]] > a:
                s.append(i)
        for j in range(len(nums))[::-1]:
            while s and nums[s[-1]] <= nums[j]:
                res = max(res, j - s.pop())
        return res