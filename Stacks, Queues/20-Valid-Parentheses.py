class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        # for char in s:
        #     if char in '({[':
        #         stk.append(char)
        #     else:
        #         if not stk:
        #             return False

        #         x = stk.pop()
        #         if (x == '(' and char == ')') or (x == '{' and char == '}') or (x == '[' and char == ']'):
        #             continue
        #         else:
        #             return False
        # return not stk
        mapping={\)\:\(\,\}\:\{\,\]\:\[\}
        for char in s:
            if char in mapping.values():
                stk.append(char)
            elif char in mapping.keys():
                if not stk or mapping[char]!=stk.pop():
                    return False
        return not stk
            
        