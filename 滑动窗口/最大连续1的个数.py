"""
Author: ByronVon
Date: 2023-08-15 01:04:52
FilePath: /leetcode/滑动窗口/最大连续1的个数.py
Description: 
"""


def MergeOnes(nums):
    merge = []
    prevs = 0
    for num in nums:
        if num:
            prevs += num
        else:
            if prevs:
                merge.append(prevs)
                prevs = 0
            merge.append(num)
    if prevs:
        merge.append(prevs)
    return merge


def LongestOnes(nums, k):
    # 给定一个二进制数组 nums 和一个整数 k，
    # 如果可以翻转最多 k 个 0 ，则返回 数组中连续 1 的最大个数
    ## 考虑先将所有的连续1求和，然后在长度为K的窗中求翻转后的最值
    news = MergeOnes(nums)
    print(news)
    # 在最小的窗口K中，不用考虑是否可以合并那么多零，因为k>=区间中零的个数
    maxs = SumOnes(news[:k])  # 窗口怎么划分呢，可以变化，从0到k+1
    for i in range(1, len(news) - k + 1):
        print(nums[i : i + k])
        curr = SumOnes(news[i : i + k])
        maxs = max(curr, maxs)
    print(maxs)
    return maxs


def SumOnes(nums):
    return sum([1 if not _ else _ for _ in nums])


def LongestOnes2(nums, k):
    # 初始化两个指针，分别指向窗口的左边界和右边界，zero_count记录0的个数
    # 每个窗口中，0的个数应该小于等于K，这个insight很关键
    left = 0
    zero_count = 0
    max_length = 0  # 最大值等于窗口长度，right-left+1
    for right in range(len(nums)):
        if nums[right] == 0:
            zero_count += 1
        while zero_count > k:
            if nums[left] == 0:
                zero_count -= 1
            left += 1
        max_length = max(max_length, right - left + 1)
    return max_length


if __name__ == "__main__":
    LongestOnes([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2)
    LongestOnes([0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], 3)
    pass
