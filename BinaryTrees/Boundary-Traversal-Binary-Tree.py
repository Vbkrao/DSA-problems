"""
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""
def isLeaf(node):
    if not node.left and not node.right:
        return True
    return False

def leftBoundary(root, ans):
    cur = root.left
    while cur:
        if not isLeaf(cur):
            ans.append(cur.data)
        if cur.left:
            cur = cur.left
        else:
            cur = cur.right

def leafNodes(root, ans):
    if not root:
        return
    if isLeaf(root):
        ans.append(root.data)
    leafNodes(root.left, ans)
    leafNodes(root.right, ans)

def rightBoundary(root, ans):
    cur = root.right
    temp = []
    while cur:
        if not isLeaf(cur):
            temp.append(cur.data)
        if cur.right:
            cur = cur.right
        else:
            cur = cur.left

    len_temp = len(temp)
    for i in range(len_temp - 1, -1, -1):
        ans.append(temp[i])
class solution:
    def boundaryTraversal(self,root):
        ans = []
        if not root:
            return ans
    
        if not isLeaf(root):
            ans.append(root.data)
    
        leftBoundary(root, ans)
        leafNodes(root, ans)
        rightBoundary(root, ans)
    
        return ans
        
