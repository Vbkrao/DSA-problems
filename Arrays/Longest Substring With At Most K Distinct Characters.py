# Problem Statement
# You are given a string s of length n, and an integer k. Your task is to find the length of the longest substring that contains at most k distinct characters.

# If k = 0, the result should be 0 since no substring can have zero distinct characters.

class solution:
    def longestSubstring(self, s, k):
        #Write your code here...
        n = len(s)
        ans = 0
        m = {}
    
        for j in range(n):
            m[s[j]] = m.get(s[j], 0) + 1
            
            if len(m) > k:
                m[s[j - ans]] -= 1
                if m[s[j - ans]] == 0:
                    del m[s[j - ans]]
            
            else:
                ans += 1
    
        return ans
