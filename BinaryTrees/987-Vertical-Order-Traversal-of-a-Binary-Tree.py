from collections import defaultdict,deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        m = defaultdict(lambda: defaultdict(list))
        q = deque([(root, (0, 0))])
        
        while q:
            cur, (row, col) = q.popleft()
            m[col][row].append(cur.val)
            
            if cur.left:
                q.append((cur.left, (row + 1, col - 1)))
            if cur.right:
                q.append((cur.right, (row + 1, col + 1)))
        
        ans = []
        for col in sorted(m):
            temp1 = []
            for row in sorted(m[col]):
                temp2 = sorted(m[col][row])
                temp1.extend(temp2)
            ans.append(temp1)
        return ans
        