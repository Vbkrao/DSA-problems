class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def convert(st):
            res=[]
            for char in st:
                if char=="#":
                    if res:
                        res.pop()
                else:
                    res.append(char)
            return "".join(res)
        return convert(s)==convert(t)
    
