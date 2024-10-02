def priority(ch):
    if ch == '^':
        return 3
    if ch in '*/':
        return 2
    if ch in '+-':
        return 1
    return -1
class Solution:
    def infixToPostfix(self, s):
        stk = []
        output = ""
            
        for ch in s:
            if ch.isalnum():  
                output += ch
            elif ch == '(':
                stk.append(ch)
            elif ch == ')':
                while stk and stk[-1] != '(':
                    output += stk.pop()
                stk.pop()  
            else:
                while stk and priority(ch) <= priority(stk[-1]):
                    output += stk.pop()
                stk.append(ch)
            
        while stk:
            output += stk.pop()
            
        return output