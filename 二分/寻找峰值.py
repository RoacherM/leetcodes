"""
Author: ByronVon
Date: 2023-08-16 17:09:05
FilePath: /leetcode/二分/寻找峰值.py
Description
"""


def findPeakElement(nums):
    # 必须使用O(logn)的时间复杂度解决该问题
    # nums[-1]=nums[n]=float('-inf')
    left, right = 0, len(nums) - 1
    while left < right:  # 当left=right时，意味着找到了峰值
        mid = (left + right) // 2
        print(f"{left}-{right}, {mid}")
        # 当mid>mid+1时，往左区间搜索
        if nums[mid] > nums[mid + 1]:
            right = mid
        else:
            left = mid + 1
    return left


if __name__ == "__main__":
    print(findPeakElement([1, 2, 3, 1]))
