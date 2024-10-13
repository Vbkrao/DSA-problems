from collections import OrderedDict, deque
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
'''

class solution:
    def topView(self, root):
        #Write your code here...
        m = OrderedDict()
        q = deque([(root, 0)])
        
        while q:
            curr, col = q.popleft()
            
            if col not in m:
                m[col] = curr.data
                
            if curr.left:
                q.append((curr.left, col - 1))
            if curr.right:
                q.append((curr.right, col + 1))
        
        ans = [data for col, data in sorted(m.items())]
        return ans