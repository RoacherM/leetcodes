"""
Author: ByronVon
Date: 2023-08-02 18:59:24
FilePath: /leetcode/数组和字符串/字符串的最大公共因子.py
Description: https://leetcode.cn/problems/greatest-common-divisor-of-strings/?envType=study-plan-v2&envId=leetcode-75
"""

# 返回可以同时除尽str1和str2的最长子串

import math


def gcdString(str1, str2):
    # 先计算最大公因子，然后获取最大公共子串，看能否被str1/str2除尽
    common = math.gcd(len(str1), len(str2))
    strc = str1[:common]
    if len(str1) // common * strc == str1 and len(str2) // common * strc == str2:
        return strc
    return ""


def gcdString2(str1, str2):
    # 分别计算str1和str2的最大重复子串，然后比较，用KMP实现
    pass


def gcdString3(str1, str2):
    # 暴力遍历哦
    pass


if __name__ == "__main__":
    str1 = "ABCABC"
    str2 = "ABC"

    print(gcdString(str1, str2))
