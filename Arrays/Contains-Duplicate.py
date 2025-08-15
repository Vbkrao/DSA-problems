class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # nums.sort()
        # n=len(nums)
        # for i in range(1,n):
        #     if nums[i]==nums[i-1]:
        #         return True
        # return False
        # O(nlogn)

        # seen=set()
        # for num in nums:
        #     if num in seen:
        #         return True
        #     seen.add(num)
        # return False
        # O(n)

        nums_dict={}
        for num in nums:
            if num not in nums_dict:
                nums_dict[num]=0
            nums_dict[num]+=1
        for num, count in nums_dict.items():
            if count>1:
                return True
        return False




