class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        stk = []
        ans = [-1] * n
    
        for i in range(2 * n - 1, -1, -1):
            while stk and nums[i % n] >= stk[-1]:
                stk.pop()
            if i < n and stk:
                ans[i] = stk[-1]
            stk.append(nums[i % n])
    
        return ans
        