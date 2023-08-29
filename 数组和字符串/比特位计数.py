"""
Author: ByronVon
Date: 2023-08-10 14:34:42
FilePath: /leetcode/其他/比特位计数.py
Description: https://leetcode.cn/problems/counting-bits/?envType=study-plan-v2&envId=leetcode-75
"""


def countBits(n):
    # 返回从[0, n]的每个数字i对应的二进制中1的个数
    return [sum(convert_to_binary(_)) for _ in range(n + 1)]


def convert_to_binary(i):
    res = []
    while i > 0:
        rem = i % 2
        res.append(rem)
        i = i // 2
    return res[::-1]  # 这里顺序是反的，


if __name__ == "__main__":
    print(countBits(5))
