class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        n = len(nums)
    
        nse = [0] * n
        stk = []
        
        for i in range(n - 1, -1, -1):
            while stk and nums[stk[-1]] >= nums[i]:
                stk.pop()
            if not stk:
                nse[i] = n
            else:
                nse[i] = stk[-1]
            stk.append(i)
        
        stk.clear()
        
        pse = [0] * n
        for i in range(n):
            while stk and nums[stk[-1]] > nums[i]:
                stk.pop()
            if not stk:
                pse[i] = -1
            else:
                pse[i] = stk[-1]
            stk.append(i)
        
        stk.clear()
        
        nge = [0] * n
        for i in range(n - 1, -1, -1):
            while stk and nums[stk[-1]] <= nums[i]:
                stk.pop()
            if not stk:
                nge[i] = n
            else:
                nge[i] = stk[-1]
            stk.append(i)
        
        stk.clear()
        
        pge = [0] * n
        for i in range(n):
            while stk and nums[stk[-1]] < nums[i]:
                stk.pop()
            if not stk:
                pge[i] = -1
            else:
                pge[i] = stk[-1]
            stk.append(i)
        
        total_sum = 0
        for i in range(n):
            total_sum += ((nge[i] - i) * (i - pge[i]) - (nse[i] - i) * (i - pse[i])) * nums[i]
        
        return total_sum
        