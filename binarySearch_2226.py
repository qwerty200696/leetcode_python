from typing import List
"""
2226. 每个小孩最多能分到多少糖果
https://leetcode-cn.com/problems/maximum-candies-allocated-to-k-children/
"""


class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        if sum(candies) < k:
            return 0
        max_candies = max(sum(candies) // k, max(candies))

        # print(max_candies)

        def get_k(candies, c):
            if c <= 0:
                return 0
            res = 0
            for j in candies:
                if j >= c:
                    res += j // c
            return res

        l, r = 0, max_candies+1  # 二分搜索，右侧边界。
        while l < r:
            mid = l + (r - l) // 2
            cur_k = get_k(candies, mid)
            # print(l, r, mid, cur_k)
            if cur_k == k:
                l = mid + 1
            elif cur_k > k:
                l = mid + 1
            elif cur_k < k:
                r = mid
        return r-1  # 注意返回的是r-1

a= [1,2,6,8,6,7,3,5,2,5]
# a= [5,8,6]
b = 3
r = Solution().maximumCandies(a, b)
print(r)
