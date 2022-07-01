
"""

752. 打开转盘锁
https://leetcode-cn.com/problems/open-the-lock/

双向BFS的练习

"""
import time
from typing import List
from queue import Queue


def plus_one(s, index):
    s = s[:index] + str((int(s[index]) + 1) % 10) + s[index + 1:]  # s[index] = (int(s[index]) + 1) % 10
    return s


def minus_one(s, index):
    new = "9" if s[index] == "0" else str((int(s[index]) - 1))
    s = s[:index] + new + s[index + 1:]
    return s


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        """"""

        deadends_set = set(deadends)
        visited = set()
        q = Queue()

        s = "0000"
        q.put(s)
        visited.add(s)
        step = 0

        while q.qsize() > 0:
            sz = q.qsize()
            for _ in range(sz):
                cur = q.get()
                if cur in deadends_set:  # 不能出现这些
                    continue
                if cur == target:  # 找到则返回
                    return step

                for j in range(4):
                    up = plus_one(cur, j)
                    if up not in visited:
                        visited.add(up)
                        q.put(up)
                    down = minus_one(cur, j)
                    if down not in visited:
                        visited.add(down)
                        q.put(down)
            step += 1
        return -1

    def openLock2(self, deadends, target):
        """双向BFS"""
        dead_set = set(deadends)
        visited = set()
        q1 = set()
        q2 = set()

        step = 0
        q1.add("0000")
        q2.add(target)

        while len(q1) > 0 and len(q2) > 0:
            tmp = set()
            for cur in q1:
                if cur in dead_set:
                    continue
                if cur in q2:
                    return step
                visited.add(cur)
                for j in range(4):
                    up = plus_one(cur, j)
                    if up not in visited:
                        # visited.add(up)
                        tmp.add(up)
                    down = minus_one(cur, j)
                    if down not in visited:
                        # visited.add(down)
                        tmp.add(down)
            step += 1
            q1 = q2
            q2 = tmp
        return -1


if __name__ == '__main__':
    deadends = ["0201", "0101", "0102", "1212", "2002"]  # 6
    target = "0202"
    #
    # deadends = ["8888"]  # 1
    # target = "0009"

    # deadends = ["8887", "8889", "8878", "8898", "8788", "8988", "7888", "9888"]
    # target = "8888"
    #
    # t1 = time.time()
    # ss = Solution().openLock(deadends, target)
    # print(ss, time.time()-t1)
    t2 = time.time()
    ss = Solution().openLock2(deadends, target)
    print(ss, time.time()-t2)
