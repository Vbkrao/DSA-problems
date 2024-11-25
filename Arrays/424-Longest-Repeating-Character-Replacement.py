class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        i, j, ans, maxi = 0, 0, 0, 0
        arr = [0] * 26

        while j < n:
            arr[ord(s[j]) - ord('A')] += 1
            maxi = max(maxi, arr[ord(s[j]) - ord('A')])

            if j - i + 1 - maxi > k:
                arr[ord(s[i]) - ord('A')] -= 1
                i += 1

            if j - i + 1 - maxi <= k:
                ans = max(ans, j - i + 1)

            j += 1

        return ans
