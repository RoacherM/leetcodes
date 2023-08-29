"""
Author: ByronVon
Date: 2023-08-23 10:58:47
FilePath: /leetcode/数据结构/统计点对的数目.py
Description: 
"""

from collections import Counter


def countPairs(n, edges, queries):
    # 第一步，先找(a,b)之间的非重叠边数目
    # 其实就是求每个节点的度，去除重复后，计算和两数之和大于queries[i]的个数
    # 可以先对deg排序，然后用双指针解决这个问题
    # 重复的次数可以遍历每一条边，然后设x-y在edges中出现了c次，c即为重复次数
    # deg[i]表示与点i相连的边的数目
    # 统计度的方式，
    deg = [0] * (n + 1)
    for x, y in edges:
        deg[x] += 1
        deg[y] += 1
    print(f"deg: {deg}")

    # 统计每条边的出现次数，(1,2)(2,1)为一条边
    cnt_e = Counter(tuple(sorted(e)) for e in edges)

    ans = [0] * len(queries)
    sorted_deg = sorted(deg)
    for j, q in enumerate(queries):
        left, right = 1, n
        while left < right:
            if sorted_deg[left] + sorted_deg[right] <= q:
                left += 1
            else:
                ans[j] += right - left
                right -= 1
        for (x, y), c in cnt_e.items():
            if q < deg[x] + deg[y] <= q + c:
                ans[j] -= 1
    print(ans)
    return ans


if __name__ == "__main__":
    countPairs(n=4, edges=[[1, 2], [2, 4], [1, 3], [2, 3], [2, 1]], queries=[2, 3])
    countPairs(
        n=5,
        edges=[[1, 5], [1, 5], [3, 4], [2, 5], [1, 3], [5, 1], [2, 3], [2, 5]],
        queries=[1, 2, 3, 4, 5],
    )
