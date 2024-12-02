class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        k = 0
        n = len(strs)
        if n == 0:
            return \\
        if n == 1:
            return strs[0]
        
        while True:
            for i in range(1, n):
                if k == len(strs[i]) or k == len(strs[0]):
                    return strs[0][:k]
                if strs[i][k] != strs[0][k]:
                    return strs[0][:k]
            
            k += 1