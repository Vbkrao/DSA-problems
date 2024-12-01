from collections import defaultdict
class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        prefixSumMap = defaultdict(int)
        prefixSumMap[0] = 1
        currentSum = 0
        ans = 0

        for num in nums:
            currentSum += num

            if (currentSum - goal) in prefixSumMap:
                ans += prefixSumMap[currentSum - goal]

            prefixSumMap[currentSum] += 1

        return ans

