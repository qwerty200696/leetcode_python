import time


class Solution:
    cnt_dict = {}
    # cnt_dict = {-1: 1, 0: 1, 1: 1, 2:2, 3:5, 4:14}

    def numTrees(self, n: int) -> int:
        """"""
        return self.count(1, n)

    def count(self, left, right):
        """ """
        if left > right:
            return 1
        cur_count = 0
        for i in range(left, right+1):  # 以i为根节点 [left, right]
            cur_left = self.count(left, i-1)
            cur_right = self.count(i+1, right)
            cur_count += cur_left * cur_right
        return cur_count

    def numTrees2(self, n: int) -> int:
        """"""
        return self.count2(1, n)

    def count2(self, left, right):
        """ """
        if left > right:
            return 1
        if right - left in self.cnt_dict.keys():
            return self.cnt_dict[right-left]
        cur_count = 0
        for i in range(left, right+1):  # 以i为根节点 [left, right]
            cur_left = self.count2(left, i-1)
            cur_right = self.count2(i+1, right)
            cur_count += cur_left * cur_right
        # if not right-left in self.cnt_dict.keys():
        self.cnt_dict[right-left] = cur_count
        return cur_count


if __name__ == '__main__':
    t1 = time.time()
    res = Solution().numTrees(15)  # 42
    # res = Solution().count(1, 4)
    t2 = time.time()
    print(res, t2-t1)

    t1 = time.time()
    s = Solution()
    res = s.numTrees2(15)  # 42
    print(s.cnt_dict.keys())
    print(s.cnt_dict.values())
    # res = Solution().count(1, 4)
    t2 = time.time()
    print(res, t2 - t1)