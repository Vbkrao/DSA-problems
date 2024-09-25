def inorder(root, k, count, ans):
    if not root:
        return

    inorder(root.left, k, count, ans)

    if count[0] == k:
        ans[0] = root.data
    count[0] += 1

    inorder(root.right, k, count, ans)

def kthSmallest(root, k):
    ans = [-1]
    count = [1]
    inorder(root, k, count, ans)
    return ans[0]