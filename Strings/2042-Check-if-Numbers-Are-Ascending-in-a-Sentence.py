class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        nums=['0','1','2','3','4','5','6','7','8','9']
        s=s.split(' ')
        next_min=-1
        for i in range(len(s)):
            if s[i][0] in nums:
                temp=int(s[i])
                if temp>next_min:
                    next_min=temp
                else:
                    return False
        return True
            