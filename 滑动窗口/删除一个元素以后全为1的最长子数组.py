"""
Author: ByronVon
Date: 2023-08-15 01:54:25
FilePath: /leetcode/滑动窗口/删除一个元素以后全为1的最长子数组.py
Description: 
"""


def longestSubarray(nums):
    # 给你一个二进制数组 nums ，你需要从中删掉一个元素。
    # 请你在删掉元素的结果数组中，返回最长的且只包含 1 的非空子数组的长度。
    # 如果不存在这样的子数组，请返回 0 。
    ## :nums[i] 要么是 0 要么是 1
    ## :必须要删掉一个元素
    left = 0
    zero = 0  # 最多能删掉的个数
    maxs = 0
    for right in range(len(nums)):
        # print(f"{left}:{right}, {nums[left:right]}, {zero}")
        if nums[right] == 0:
            if zero:  # 如果zero已经有值，则计算窗口内1的个数
                # print(nums[left:right], zero)
                curr = right - left - 1  # 删掉了一个
                maxs = max(curr, maxs)
                # 左端点移动，一直移动过第一个zero
                while zero:
                    if not nums[left]:
                        zero -= 1
                    left += 1
            zero += 1
    # print(f"{left}:{len(nums)} {nums[left:]}, {maxs}")
    # print("*" * 10)
    maxs = max(maxs, len(nums) - left - 1)
    print(maxs)
    return maxs


def longestSubarray2(nums):
    left, right = 0, 0
    zero_count = 0
    max_len = 0

    for right in range(len(nums)):
        if nums[right] == 0:
            zero_count += 1

        while zero_count > 1:  # 当窗口内的0数量超过1时，需要移动左边界
            if nums[left] == 0:
                zero_count -= 1
            left += 1

        # 更新最大长度，需要减1以考虑到我们需要删除一个元素
        max_len = max(max_len, right - left)

    return max_len


if __name__ == "__main__":
    longestSubarray2([1, 1, 0, 1])
    longestSubarray2([1, 1, 1])
    longestSubarray2([0, 1, 1, 1, 0, 1, 1, 0, 1])
    longestSubarray2([1, 1, 0])
    longestSubarray2([0, 0, 0])
    longestSubarray2([0])
    longestSubarray2([1])
    longestSubarray2([1, 0, 1, 0, 1, 1, 1, 1, 1, 0])
    longestSubarray2([1, 1, 0, 1, 1, 1, 0, 1, 1, 1])
