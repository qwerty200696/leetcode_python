"""

700. 二叉搜索树中的搜索
https://leetcode-cn.com/problems/search-in-a-binary-search-tree/

"""
import time
from typing import Optional
from tree_plot import draw, build_tree


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    target = None
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        """"""
        if not root:
            return None
        if root.val == val:
            self.target = root
        elif root.val > val:
            self.searchBST(root.left, val)
        else:
            self.searchBST(root.right, val)

        return self.target

    def searchBST2(self, root: TreeNode, val: int) -> TreeNode:
        """"""
        if not root:
            return None
        if root.val > val:
            return self.searchBST(root.left, val)
        elif root.val < val:
            return self.searchBST(root.right, val)

        return root


if __name__ == '__main__':
    # root = [4, 2, 7, 1, 3]  # [2,1,3]
    # val = 2
    # root = build_tree(root)
    # res = Solution().searchBST(root, val)
    # draw(res)

    root = [18, 2, 22, None, None, None, 63, None, 84, None, None]
    val = 63
    root = build_tree(root)
    t1 = time.time()
    res2 = Solution().searchBST(root, val)
    t2 = time.time()
    res3 = Solution().searchBST2(root, val)
    t3 = time.time()
    print(t2-t1)
    print(t3-t2)