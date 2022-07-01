from typing import Optional
from tree_plot import draw, build_tree
from queue import Queue

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        """"""
        if not root:
            return 0
        q = Queue()
        q.put(root)
        depth = 1
        while q:
            sz = q.qsize()
            for i in range(sz):
                cur_node = q.get()
                if not cur_node.left and not cur_node.right:  # 一层层筛查的，这个肯定是最早发现的
                    return depth
                if cur_node.left:
                    q.put(cur_node.left)
                if cur_node.right:
                    q.put(cur_node.right)
            depth += 1
        return depth


if __name__ == '__main__':
    root = [3, 9, 20, None, None, 15, 7]
    root = [2, None, 3, None, 4, None, 5, None, 6]
    tree = build_tree(root)
    draw(tree)
    rr = Solution().minDepth(tree)
    print(rr)
