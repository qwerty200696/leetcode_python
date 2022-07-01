from typing import Optional
from tree_plot import draw, build_tree
"""
1038. 从二叉搜索树到更大和树
https://leetcode-cn.com/problems/binary-search-tree-to-greater-sum-tree/

538. 把二叉搜索树转换为累加树
https://leetcode-cn.com/problems/convert-bst-to-greater-tree/
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    sum = 0
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """"""
        self.traverse_r(root)
        return root

    def traverse(self, root):  # 从小到大遍历
        if not root:
            return
        self.traverse(root.left)
        print(root.val, end=" ")
        self.traverse(root.right)

    def traverse_r(self, root):  # 从大到小遍历
        if not root:
            return
        self.traverse_r(root.right)  # TODO right在前，就是降序了
        self.sum += root.val
        root.val = self.sum
        print("{}({})".format(root.val, self.sum), end=" ")
        self.traverse_r(root.left)


if __name__ == '__main__':
    root = [4, 1, 6, 0, 2, 5, 7, None, None, None, 3, None, None, None, 8]
    root = build_tree(root)  # 层序遍历建树
    # Solution().traverse(root)
    print()
    Solution().traverse_r(root)
    # print(res)
    draw(root)


