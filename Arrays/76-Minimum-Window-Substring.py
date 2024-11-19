class Solution:
    def minWindow(self, s: str, t: str) -> str:
        from collections import Counter
        m = Counter(t)
        n = len(s)

        start_idx = -1
        length = float('inf')
        i = 0
        j = 0
        count = 0

        while j < n:
            if m[s[j]] > 0:
                count += 1
            m[s[j]] -= 1

            while count == len(t):
                if j - i + 1 < length:
                    length = j - i + 1
                    start_idx = i

                m[s[i]] += 1
                if m[s[i]] > 0:
                    count -= 1
                i += 1

            j += 1

        return \\ if start_idx == -1 else s[start_idx:start_idx + length]
        