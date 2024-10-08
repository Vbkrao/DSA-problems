class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic={}
        for i,num in enumerate(nums):
            x=target-num
            if x in dic:
                return [dic[x],i]
            else:
                dic[num]=i
        return [-1,-1]
        