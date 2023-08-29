"""
Author: ByronVon
Date: 2023-08-15 14:23:20
FilePath: /leetcode/数据结构/相等行列对.py
Description: 
"""


def equalPairs(grid):
    # 判断NXN矩阵的整数矩阵grid，R_i行和C_j列相等的行列对(R_i, C_j)的数目
    # 分别按照行遍历，然后计算和列一致的数目，记录在same中
    same = set()
    for c in range(len(grid)):
        c_ = grid[c]  # 行
        for r in range(len(grid)):
            r_ = [g[r] for g in grid]  # 列
            print(c_, r_)
            if c_ == r_:
                same.add((c, r))
    return len(same)


def equalPairs2(grid):
    # 优化思路：
    # 1、减少冗余的列的创建，事先构建一个转置矩阵
    # 2、通过计算行和列的hash来进行比较
    n = len(grid)
    rows = [hash(str(grid[r])) for r in range(n)]
    columns = [hash(str([grid[r][c] for r in range(n)])) for c in range(n)]
    # 不用用结合存储结果，因为(R_i, C_j)不可能重复出现
    same = 0
    for c in range(n):
        for r in range(n):
            if rows[c] == columns[r]:
                same += 1
    return same


if __name__ == "__main__":
    print(equalPairs2([[3, 2, 1], [1, 7, 6], [2, 7, 7]]))
    print(equalPairs2([[3, 1, 2, 2], [1, 4, 4, 5], [2, 4, 2, 2], [2, 4, 2, 2]]))
