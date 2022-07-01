import time
from typing import Optional
from tree_plot import draw, build_tree


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BST:
    def __init__(self):
        pass

    def add(self, root, val):
        if not root:
            return TreeNode(val)
        if root.val < val:
            root.right = self.add(root.right, val)
        elif root.val > val:
            root.left = self.add(root.left, val)
        return root

    def get_min(self, root):  # 左边的是最小的节点
        while root.left:
            root = root.left
        return root

    def delete(self, root, val):
        if not root:
            return None
        if root.val == val:
            if not root.left and not root.right:
                return None
            elif not root.left:
                return root.right
            elif not root.right:
                return root.left
            min_node = self.get_min(root.right)
            # root.val = min_node.val  # 为什么不直接替换val的值？是为了通用性。
            root.right = self.delete(root.right, min_node.val)
            min_node.left = root.left
            min_node.right = root.right
            root = min_node
        elif root.val > val:
            root.left = self.delete(root.left, val)
        elif root.val < val:
            root.right = self.delete(root.right, val)
        return root


if __name__ == '__main__':
    root = [3, 1, 5, None, None, 4, 6]
    root = build_tree(root)
    root = BST().add(root, 2)
    root = BST().add(root, 7)
    root = BST().add(root, 8)
    draw(root)
    root = BST().delete(root, 6)
    draw(root)

