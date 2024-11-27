class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        # Helper function to find the number of subarrays with at most 'k' distinct integers
        def atMostKDistinct(nums, k): 
            n = len(nums) 
            l, r = 0, 0  
            window_map = {}  # Dictionary to keep track of the count of elements in the current window
            ans = 0  

            while r < n: 
                # Add current element to the window
                if nums[r] not in window_map:  
                    window_map[nums[r]] = 1  
                else:
                    window_map[nums[r]] += 1 

                # Shrink the window from the left if it has more than 'k' distinct elements
                while len(window_map) > k:  
                    window_map[nums[l]] -= 1  # Reduce the count of the leftmost element
                    if window_map[nums[l]] == 0:  # If its count reaches zero, remove it from the window
                        del window_map[nums[l]]  
                    l += 1 

                # The window is now valid (with <= 'k' distinct integers), count all subarrays ending at 'r'
                ans += (r - l + 1)
                r += 1  

            return ans
        
        # The result is the number of subarrays with exactly 'k' distinct integers
        # Calculated as the difference between subarrays with at most 'k' distinct
        # and subarrays with at most 'k-1' distinct (which removes over-counting)
        return atMostKDistinct(nums, k) - atMostKDistinct(nums, k-1)