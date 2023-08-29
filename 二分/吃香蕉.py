"""
Author: ByronVon
Date: 2023-08-16 18:04:56
FilePath: /leetcode/二分/吃香蕉.py
Description: https://leetcode.cn/problems/koko-eating-bananas/?envType=study-plan-v2&envId=leetcode-75
"""


def minEatingSpeed(piles, h):
    # 然后计算piles[i]和h的倍数关系
    # 维护一个eat[i]的数组，每个值表示吃掉这一堆需要的时间
    # 求min(eat[i])
    # 先排序值为最小的值为x
    # times = [-(-p // x) for p in piles]
    # 求 sum(times) <= h
    # 求 min(x)
    # 这是数值解法，用二分在(1, max_p)中搜一个最下的答案出来
    piles.sort()
    left, right = 1, piles[-1]
    # 从left<->right中直接搜出来答案
    while left < right:
        mid = (left + right) // 2
        tim = [-(-p // mid) for p in piles]
        # print(tim, mid, f"{left}-{right}")
        if sum(tim) > h:  # 如果消耗的时间比h大，需要加快速度
            left = mid + 1
        else:
            right = mid
    print(left)
    return left


if __name__ == "__main__":
    minEatingSpeed([3, 6, 7, 11], 8)
    minEatingSpeed([30, 11, 23, 4, 20], 5)
    minEatingSpeed([30, 11, 23, 4, 20], 6)
    minEatingSpeed([312884470], 312884469)
    minEatingSpeed(
        [
            332484035,
            524908576,
            855865114,
            632922376,
            222257295,
            690155293,
            112677673,
            679580077,
            337406589,
            290818316,
            877337160,
            901728858,
            679284947,
            688210097,
            692137887,
            718203285,
            629455728,
            941802184,
        ],
        823855818,
    )
    minEatingSpeed([1000000000, 1000000000], 3)
