"""
Author: ByronVon
Date: 2023-08-11 23:28:46
FilePath: /leetcode/数据结构/股票跨度.py
Description: https://leetcode.cn/problems/online-stock-span/?envType=study-plan-v2&envId=leetcode-75
"""

# 设计一个算法收集某些股票的每日报价，并返回该股票当日价格的 跨度 。

# 当日股票价格的 跨度 被定义为股票价格小于或等于今天价格的最大连续日数（从今天开始往回数，包括今天）。

# 例如，如果未来 7 天股票的价格是 [100,80,60,70,60,75,85]，那么股票跨度将是 [1,1,1,2,1,4,6] 。


from math import inf


class StockSpanner:
    # 本质就是求开始到现在，小于当前数值的个数
    # 返回时+1
    def __init__(self) -> None:
        pass

    def next(self, price):
        pass


def spanner(stocks):
    # 返回比到从头到当前位置，小于等于当前值的个数
    # 寻找比小于等于当前值的个数，用单调栈
    ans = []
    queue = [(-1, inf)]
    for i, stock in enumerate(stocks):
        while stock >= queue[-1][1]:
            queue.pop()
        queue.append((i, stock))
        ans.append(i - queue[-2][0])
    return ans


if __name__ == "__main__":
    print(i, price, spanner(prices))
