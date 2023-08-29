"""
Author: ByronVon
Date: 2023-08-16 14:42:31
FilePath: /leetcode/二分/咒语和药水的成功对数.py
Description: 
"""

import math


# spells[i]*potions,求每次乘积大于等于success的个数
# 并记录在pairs中返回
def successfulPairs(spells, potions, success):
    # 暴力方法：
    pairs = []
    for s in spells:
        d = math.ceil(success / s)  # 减少了运算
        num = sum(p >= d for p in potions)
        print(num)
        pairs.append(num)
    return pairs


# 优化方式，可以先排序，找到中点，根据重点和[success/s]的大小找下届
def successfulPairs2(spells, potions, success):
    pairs = []
    potions.sort()
    l = len(potions)
    for s in spells:
        d = math.ceil(success / s)
        print(d)
        k = find_lower_bound(potions, d)  #
        pairs.append(l - k)
    return pairs


# def find_lower_bound(lst, n):
#     # 找到一个数组大于等于n的最小值
#     lst.sort()  # 先排序，二分的精髓就在于排序
#     # 但其实也可以直接用二分做，当返回来的位置即可
#     l, r = 0, len(lst) - 1
#     while l <= r:
#         m = (l + r) // 2
#         # lst[m]小于n,则l=n+1,继续寻找
#         if lst[m] < n:
#             l = m + 1
#         else:
#             # lst[m]>n且lst[m-1]<n，返回lst[m]
#             # lst[0]>n，返回lst[0]
#             if m == 0 or lst[m - 1] < n:
#                 return m
#             else:
#                 r = m - 1
#     return len(lst)  # 没有小于等于n的数值


def find_lower_bound(lst, n):
    # lst已经sort,
    # 这和二分查找可以保证有多个元素时，只返回第一个相同的元素
    l, r = 0, len(lst) - 1
    while l <= r:
        m = (l + r) // 2
        if lst[m] < n:
            l = m + 1
        else:
            r = m - 1
    return l


if __name__ == "__main__":
    print(successfulPairs2([5, 1, 3], [1, 2, 3, 4, 5], 7))
    print(successfulPairs2([3, 1, 2], [8, 5, 8], 16))

    # for i in range(100):
    #     lst = list(range(i))
    #     for j in range(len(lst)):
    #         res = find_lower_bound(lst, j)
    #         if not res:
    #             print(i, j, res)
    print(find_lower_bound([1, 2, 2, 3, 4, 6, 8], 5))
