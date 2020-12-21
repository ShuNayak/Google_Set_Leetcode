class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def mergeBinaryTree(self, t1:TreeNode, t2:TreeNode)->TreeNode:
        if not t1 and not t2:
            return None
        elif not t1:
            return t2
        elif not t2:
            return t1
        root = TreeNode(t1.val+t2.val)
        root.left = TreeNode(t1.left, t2.left)
        root.right = TreeNode(t1.right, t2.right)
        return root

obj = Solution()
t1 = TreeNode(1)
t1.left = TreeNode(2)
t1.left.left = TreeNode(3)

t2 = TreeNode(1)
t2.right = TreeNode(2)
t2.right.right = TreeNode(3)

root = obj.mergeBinaryTree(t1, t2)
print(root.val)
