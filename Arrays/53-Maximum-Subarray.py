class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #Kadane's Algo:O(n)
        maxSum=nums[0]
        curSum=0
        for i in nums:
            curSum=max(curSum,0)
            curSum+=i
            maxSum=max(maxSum,curSum)
        return maxSum

        