"""
Author: ByronVon
Date: 2023-08-11 22:08:06
FilePath: /leetcode/数组和字符串/最少数量的气球.py
Description: https://leetcode.cn/problems/minimum-number-of-arrows-to-burst-balloons/?envType=study-plan-v2&envId=leetcode-75
"""


def findMinArrowShots(points):
    # 用最少的箭将气球引爆
    # points[i] = [x_start, x_end], x_start<x_end
    # 其实类似合并区间，如果能合并，则更新合并后的共同区间，若不能合并，则新增该元素
    ## 先排序
    points = sorted(points, key=lambda i: i[0])
    queues = [points[0]]
    for i in range(1, len(points)):
        curr = points[i]
        tail = queues[-1]
        if curr[0] <= tail[1]:  # 若二者存在交集，则更新区间
            queues[-1] = [max(tail[0], curr[0]), min(tail[1], curr[1])]
        else:
            queues.append(curr)
    # print(queues)
    return len(queues)


if __name__ == "__main__":
    findMinArrowShots([[10, 16], [2, 8], [1, 6], [7, 12]])
    findMinArrowShots([[1, 2], [3, 4], [5, 6], [7, 8]])
    findMinArrowShots([[1, 2], [2, 3], [3, 4], [4, 5]])
