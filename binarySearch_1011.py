from typing import List


class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        def get_days(w, k):
            d, tmp_sum = 0, 0
            for i in w:
                if tmp_sum + i == k:
                    tmp_sum = 0
                    d += 1
                elif tmp_sum + i < k:
                    tmp_sum += i
                    continue
                elif tmp_sum + i > k:
                    d += 1
                    tmp_sum = i
            if tmp_sum != 0:
                d += 1
            return d

        def get_days2(w, k):  # 更为简介的写法
            i, d = 0, 0
            while i < len(w):
                cap = k
                while i < len(w):
                    if cap < w[i]:
                        break
                    else:
                        cap -= w[i]
                    i += 1
                d += 1
            return d

        left, right = max(weights), sum(weights)  # 每天搬动数
        while left <= right:
            mid = left + (right - left) // 2
            cur_day = get_days2(weights, mid)
            if cur_day == days:  # 寻找左边界
                right = mid - 1
            elif cur_day > days:
                left = mid + 1
            elif cur_day < days:
                right = mid - 1

        return left


if __name__ == '__main__':
    weights, days = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5
    res = Solution().shipWithinDays(weights, days)  # 15
    print(res)
    weights, days = [3, 2, 2, 4, 1, 4], 3
    res = Solution().shipWithinDays(weights, days)  # 6
    print(res)
    weights, days = [1, 2, 3, 1, 1], 4
    res = Solution().shipWithinDays(weights, days)  # 3
    print(res)
    weights, days = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10
    res = Solution().shipWithinDays(weights, days)  # 10
    print(res)
