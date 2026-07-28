# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSame(node1, node2):
            if not node1 and not node2:
                return True

            if not node1 or not node2:
                return False

            if node1.val != node2.val:
                return False

            # Check both left and right subtrees
            return isSame(node1.left, node2.left) and isSame(node1.right, node2.right)

        # Edge cases
        if not subRoot:
            return True

        if not root:
            return False

        # Check if subtree starts here
        if isSame(root, subRoot):
            return True

        # Otherwise search left or right
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)