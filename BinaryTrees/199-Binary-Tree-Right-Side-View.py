from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = deque([root])

        ans = []
        if not root:
            return ans

        while q:
            length = len(q)
            temp = None

            for i in range(length):
                cur = q.popleft()
                temp = cur.val

                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)

            ans.append(temp)
        return ans
        