"""
Author: ByronVon
Date: 2023-08-08 20:39:06
FilePath: /leetcode/双指针/判断是否为子序列.py
Description: https://leetcode.cn/problems/is-subsequence/?envType=study-plan-v2&envId=leetcode-75
"""


def isSubsequence(s, t):
    # 判断s是否为t的子序列，即能否在t中的找出满足s顺序的序列
    i, j = 0, 0
    while i < len(t) and j < len(s):
        # print(f"compare: {t[i]}-{s[j]}")
        if t[i] == s[j]:
            i += 1
            j += 1
        else:
            i += 1
        # print(f"update: {i}, {j}")
    # print(i, j, len(s), len(t))
    # if j == len(s):
    # return True
    # return False
    return j == len(s)


if __name__ == "__main__":
    print(isSubsequence(s="abc", t="ahbgdc"))
    print(isSubsequence(s="axc", t="ahbgdc"))
