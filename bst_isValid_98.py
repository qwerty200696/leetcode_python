# Definition for a binary tree node.
from tree_plot import draw, build_tree


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        """"""
        return self.is_valid(root, None, None)

    def is_valid(self, root, min, max):
        """"""
        if not root:
            return True
        if min and root.val < min.val: return False
        if max and root.val > max.val: return False

        return self.is_valid(root.left, min, root) and self.is_valid(root.right, root, max)


if __name__ == '__main__':
    # root = [5, 1, 4, None, None, 3, 6]
    root = [3, 1, 5, None, None, 4, 6]
    root = build_tree(root)
    # draw(root)
    res = Solution().isValidBST(root)
    print(res)