"""
Author: ByronVon
Date: 2023-08-08 21:18:58
FilePath: /leetcode/数组和字符串/找到最高海拔.py
Description: https://leetcode.cn/problems/find-the-highest-altitude/?envType=study-plan-v2&envId=leetcode-75
"""


def largestAltitude(gain):
    gain = [0] + gain
    altitudes = [0]
    for i in range(1, len(gain)):
        altitudes.append(sum(gain[: i + 1]))
    print(altitudes)
    return max(altitudes)


def largestAltitude2(gain):
    # 写成递推的形式
    gain = [0] + gain
    altitudes = [0] * len(gain)
    for i in range(1, len(gain)):
        altitudes[i] = altitudes[i - 1] + gain[i]
    # print(altitudes)
    return max(altitudes)


if __name__ == "__main__":
    print(largestAltitude2([-5, 1, 5, 0, -7]))
    print(largestAltitude2([-4, -3, -2, -1, 4, 3, 2]))
