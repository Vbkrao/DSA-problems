# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def inorder(root,mini,maxi,ans):
    if not root:
        return
    
    inorder(root.left,mini,root.val,ans)
    
    if root.val<=mini or root.val>=maxi:
        ans[0]=False
        
    inorder(root.right,root.val,maxi,ans)
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        ans=[True]
        mini=float('-inf')
        maxi=float('inf')
        inorder(root,mini,maxi,ans)
        return ans[0]

