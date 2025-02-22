class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left=right=0
        numZeroes = 0
        longestSeq = 0

        while right < len(nums):
            if nums[right] == 0:
                numZeroes += 1

            while numZeroes > k:
                if nums[left] == 0:
                    numZeroes -= 1
                left += 1

            longestSeq = max(longestSeq, right - left + 1)
            right += 1

        return longestSeq