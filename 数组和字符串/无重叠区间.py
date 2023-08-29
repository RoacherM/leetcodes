"""
Author: ByronVon
Date: 2023-08-11 18:17:35
FilePath: /leetcode/数组和字符串/无重叠区间.py
Description: https://leetcode.cn/problems/non-overlapping-intervals/?envType=study-plan-v2&envId=leetcode-75
"""


def eraseOverlapIntervals(intervals):
    # 给定一个区间集合，其中interval[i]=[start_i, end_i]
    # 返回需要移出的最小区间数量，使得剩余的区域不再重叠
    # 只需要判断是否需要i[end]是否比i+1[start]大即可
    # 由于只需要获得最小的数目，可以考虑先排序
    intervals = sorted(intervals, key=lambda i: i[1])
    print(intervals)
    queue = [intervals[0]]
    for i in range(1, len(intervals)):
        if intervals[i][0] >= queue[-1][1]:
            queue.append(intervals[i])
        # # 采用贪心的方式做，如果二者重叠，则选择跨度较小的那个
        # elif intervals[i][1] - intervals[i][0] < queue[-1][1] - queue[-1][0]:
        #     queue[-1] = intervals[i]
        print(queue)
    print(f"out: {queue}")
    return len(intervals) - len(queue)


if __name__ == "__main__":
    case1 = [[1, 2], [2, 3], [3, 4], [1, 3], [3, 7]]
    case2 = [[1, 2], [1, 2], [1, 2]]
    case3 = [[1, 2], [2, 3]]
    case4 = [[1, 100], [11, 22], [1, 11], [2, 12]]
    case5 = [
        [-52, 31],
        [-73, -26],
        [82, 97],
        [-65, -11],
        [-62, -49],
        [95, 99],
        [58, 95],
        [-31, 49],
        [66, 98],
        [-63, 2],
        [30, 47],
        [-40, -26],
    ]

    for case in [case1, case2, case3, case4, case5]:
        # case = sorted(case, key=lambda i: (i[0], i[1]))
        # print(case)
        print(eraseOverlapIntervals(case))
