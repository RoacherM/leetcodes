"""
Author: ByronVon
Date: 2023-08-08 21:05:23
FilePath: /leetcode/双指针/盛最多水的容器.py
Description: https://leetcode.cn/problems/container-with-most-water/?envType=study-plan-v2&envId=leetcode-75
"""


def maxArea(height):
    # 求能盛最多水的容器
    # height 为一个数组，height[i]表示挡板的高度
    # Area = min(height[j], height[k]) * abs(j-k)
    # 第一种方法，暴力求解，将所有可能的情况列举出，然后取最大
    maxa = 0
    for i in range(len(height)):
        for j in range(i + 1, len(height)):
            a = (j - i) * min(height[i], height[j])
            if a > maxa:
                maxa = a
    return maxa


def maxArea2(self, height: List[int]) -> int:
    maxa = 0
    left, right = 0, len(height) - 1
    while left < right:
        h = min(height[left], height[right])
        w = right - left
        maxa = max(maxa, h * w)
        # 一开始的宽度是最大的，面积像变大的唯一可能是变高
        # 因此哪一侧端就移动谁
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return maxa


if __name__ == "__main__":
    print(maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
    print(maxArea([1, 1]))
