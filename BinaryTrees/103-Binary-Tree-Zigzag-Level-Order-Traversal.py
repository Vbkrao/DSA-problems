# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        if not root:
            return ans
        flag = True
        q = [root]
    
        while q:
            len_q = len(q)
            temp = [0] * len_q
    
            for i in range(len_q):
                cur = q.pop(0)
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
    
                if flag:
                    index = i
                else:
                    index = len_q - 1 - i
                temp[index] = cur.val
    
            ans.append(temp)
            flag = not flag
    
        return ans
        