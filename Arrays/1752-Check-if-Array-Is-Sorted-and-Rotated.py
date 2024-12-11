class Solution(object):
    def check(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        length=len(nums)
        count=0
        if nums[0]<nums[length-1]:
            count+=1
        for i in range(0,length-1):
            if nums[i]>nums[i+1]:
                count+=1
            if count>1:
                return False
        return True

        
        