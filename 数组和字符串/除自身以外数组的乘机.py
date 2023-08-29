"""
Author: ByronVon
Date: 2023-08-08 15:22:57
FilePath: /leetcode/数组和字符串/除自身以外数组的乘机.py
Description: https://leetcode.cn/problems/product-of-array-except-self/description/?envType=study-plan-v2&envId=leetcode-75
"""


def productExceptSelf(nums):
    # 返回除自身以外的余下元素的乘积，在O(n)的复杂度内完成
    # 可以先分别构造i的前缀数组和后缀数组
    length = len(nums)
    L, R, Ans = [0] * length, [0] * length, [0] * length
    # L记录前缀乘积，L[i] = nums[i-1] * L[i-1]，表示beg->i-1的连城结果
    # R记录后缀乘积，R[i] = nums[i+1] * R[i+1]，表示i+1->end的连城结果，也等价于end->i+1
    L[0] = 1
    for i in range(1, length):
        L[i] = nums[i - 1] * L[i - 1]
    # print(L)

    R[length - 1] = 1
    for i in reversed(range(length - 1)):
        R[i] = nums[i + 1] * R[i + 1]
    for i in range(length):
        Ans[i] = L[i] * R[i]
    return Ans


def productExceptSelf2(nums):
    # 将空间复杂度优化到O(1)
    length = len(nums)
    answer = [0] * length
    # 先构造前缀积
    answer[0] = 1
    for i in range(1, length):
        answer[i] = answer[i - 1] * nums[i - 1]
    # 从右端开始遍历，同时用R记录后缀乘积
    R = 1
    for i in reversed(range(length)):
        answer[i] = answer[i] * R
        R = R * nums[i]
    return answer


if __name__ == "__main__":
    print(productExceptSelf2([1, 2, 3, 4]))
