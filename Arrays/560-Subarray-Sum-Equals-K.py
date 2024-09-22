class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
            m = {}
            n = len(nums)

            sum = 0
            count = 0

            for i in range(n):
                sum += nums[i]
                if sum == k:
                    count += 1
                count += m.get(sum - k, 0)
                m[sum] = m.get(sum, 0) + 1

            return count

        