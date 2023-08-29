"""
Author: ByronVon
Date: 2023-08-10 17:41:26
FilePath: /leetcode/其他/或运算的最小翻转次数.py
Description: https://leetcode.cn/problems/minimum-flips-to-make-a-or-b-equal-to-c/?envType=study-plan-v2&envId=leetcode-75
"""


def minFlips(a, b, c):
    binary_a = convert_to_binary(a)
    binary_b = convert_to_binary(b)
    binary_c = convert_to_binary(c)
    # print(binary_a, binary_b, binary_c)
    max_len = max(len(binary_a), len(binary_b), len(binary_c))

    binary_a = "{:0>{max_len}}".format(binary_a, max_len=max_len)
    binary_b = "{:0>{max_len}}".format(binary_b, max_len=max_len)
    binary_c = "{:0>{max_len}}".format(binary_c, max_len=max_len)

    # print(binary_a, binary_b, binary_c)
    ops = 0
    for i, j, k in zip(binary_a, binary_b, binary_c):
        i, j, k = int(i), int(j), int(k)
        if i | j != k:
            if (i, j, k) == (1, 0, 0):
                ops += 1
            elif (i, j, k) == (0, 1, 0):
                ops += 1
            elif (i, j, k) == (1, 1, 0):
                ops += 2
            elif (i, j, k) == (0, 0, 1):
                ops += 1
    return ops


def convert_to_binary(i):
    binary = ""
    while i != 0:
        left = i % 2
        i = i // 2
        binary = str(left) + binary
    return binary


if __name__ == "__main__":
    print(minFlips(2, 6, 5))
    print(minFlips(4, 2, 7))
    print(minFlips(1, 2, 3))
    # print(convert_to_binary(10))
