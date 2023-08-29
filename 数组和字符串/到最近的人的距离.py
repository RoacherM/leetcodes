"""
Author: ByronVon
Date: 2023-08-22 11:42:57
FilePath: /leetcode/数组和字符串/到最近的人的距离.py
Description: 
"""


def maxDistToClosest(seats):
    # 先遍历一遍，将seats分为
    ans = 0
    tmp = []
    for i, s in enumerate(seats):
        if not s:
            tmp.append(i)
        else:
            if tmp:
                if tmp[0] == 0:
                    ans = max(len(tmp), ans)
                else:
                    # 考虑奇偶数的情况
                    ans = max((len(tmp) + 1) // 2, ans)
                    # if len(tmp) % 2 == 0:
                    #     ans = max(len(tmp) // 2, ans)
                    # else:
                    #     ans = max(len(tmp) // 2 + 1, ans)
            tmp = []
    if tmp:
        ans = max(len(tmp), ans)
    print(ans)
    return ans


def maxDistToClosest2(seats):
    ans = 0
    tmp = 0  # 直接用一个计数器而不是列表来跟踪连续的空位

    # 处理座位开始的空位

    while seats[tmp] == 0:
        tmp += 1
    ans = max(ans, tmp)

    distance = 0  # 用于跟踪中间的连续空位
    for i in range(tmp, len(seats)):
        if seats[i] == 0:
            distance += 1
        else:
            # 对于奇数，用 (distance // 2) + 1
            # 对于偶数，直接用 distance // 2
            ans = max(ans, (distance + 1) // 2)
            distance = 0

    # 处理座位结束的空位
    ans = max(ans, distance)
    print(ans)

    return ans


if __name__ == "__main__":
    seats1 = [1, 0, 0, 0, 1, 0, 1]
    seats2 = [1, 0, 0, 0]
    seats3 = [0, 1]
    seats4 = [0, 0, 1, 0]
    seats5 = [1, 0, 0, 0, 1]
    for seat in [seats1, seats2, seats3, seats4, seats5]:
        maxDistToClosest(seat)
