# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def inorder(root, k, count, ans):
        if not root:
            return

        inorder(root.left, k, count, ans)

        if count[0] == k:
            ans[0] = root.val
        count[0] += 1

        inorder(root.right, k, count, ans)


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ans = [-1]
        count = [1]
        inorder(root, k, count, ans)
        return ans[0]