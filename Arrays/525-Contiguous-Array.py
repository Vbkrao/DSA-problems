class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        mx=0
        count=0  
        countToIndex = {0:-1} 
        for i in range(len(nums)):
            if nums[i] == 1 : 
                count +=1
            else: 
                count -=1
            if count in countToIndex:
                mx=max(mx, i-countToIndex[count])
            else:
                countToIndex[count] = i  
        return mx
        