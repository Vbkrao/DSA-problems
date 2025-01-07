class Solution:
    def removeStars(self, s: str) -> str:
        stk=[]
        for char in s:
            if char=="*":
                stk.pop()
            else:
                stk+=[char]
        return "".join(stk)