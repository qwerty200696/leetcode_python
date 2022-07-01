
import time
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        return self.count(1, n)

    def count(self, left, right):
        result = []
        if left > right:
            result.append(None)
            return result
        for i in range(left, right+1):
            left_list = self.count(left, i-1)
            right_list = self.count(i+1, right)
            for l in left_list:
                for r in right_list:
                    root = TreeNode(i)
                    root.left = l
                    root.right = r
                    result.append(root)
        return result


class Solution2:
    res_dict = {}

    def generateTrees(self, n: int) -> List[TreeNode]:
        return self.count(1, n)

    def count(self, left, right):
        result = []
        if left > right:
            result.append(None)
            return result
        if (left, right) in self.res_dict.keys():
            return self.res_dict[(left, right)]
        for i in range(left, right+1):
            left_list = self.count(left, i-1)
            right_list = self.count(i+1, right)
            for l in left_list:
                for r in right_list:
                    root = TreeNode(i)
                    root.left = l
                    root.right = r
                    result.append(root)
        self.res_dict[(left, right)] = result
        print(len(self.res_dict))
        return result


if __name__ == '__main__':
    t1 = time.time()
    res = Solution().generateTrees(13)
    t2 = time.time()
    print(len(res), t2-t1)
    t1 = time.time()
    res = Solution2().generateTrees(13)
    t2 = time.time()
    print(len(res), t2-t1)
