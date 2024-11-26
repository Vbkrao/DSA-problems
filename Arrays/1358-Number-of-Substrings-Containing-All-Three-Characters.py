class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        arr = [-1, -1, -1]
        ans = 0
    
        for i in range(n):
            arr[ord(s[i]) - ord('a')] = i
            ans += min(arr) + 1
    
        return ans
        