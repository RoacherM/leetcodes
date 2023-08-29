"""
Author: ByronVon
Date: 2023-08-15 23:44:23
FilePath: /leetcode/动态规划/多米诺和托米诺平铺.py
Description: 
"""

MOD = 10**9 + 7


def numTilings(n):
    # 当面板的长度小于等于1时的特殊情况
    if n == 1:
        return 1
    f = [0] * (n + 1)  # 因为要返回n处的值
    f[0] = f[1] = 1
    f[2] = 2
    for i in range(3, n + 1):
        f[i] = (2 * f[i - 1] + f[i - 3]) % 10
    return f[n]


if __name__ == "__main__":
    print(numTilings(5))
    print(numTilings(4))
    print(numTilings(1))
