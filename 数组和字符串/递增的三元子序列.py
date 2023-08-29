"""
Author: ByronVon
Date: 2023-08-08 16:38:20
FilePath: /leetcode/数组和字符串/递增的三元子序列.py
Description: https://leetcode.cn/problems/increasing-triplet-subsequence/?envType=study-plan-v2&envId=leetcode-75
"""


def increaseTriplet(nums):
    # 注意ijk不一定需要连续，只需要递增即可
    # 暴力遍历
    for j in range(len(nums)):
        res = [nums[j]]  # res为一个递增数组
        for i in range(j + 1, len(nums)):
            # print(nums[i])
            if nums[i] > res[-1]:
                if len(res) == 1:
                    res.append(nums[i])
                else:
                    res[-1] = nums[i]
            if len(res) == 3:
                print(res)
                return True
        print(res)
    return False


def increasingTriplet2(nums):
    # 贪心大法好
    first = float("inf")
    second = float("inf")

    for num in nums:
        # 三个分支都走完才为true,确保了长度至少为3
        print(first, second)
        if num <= first:
            first = num
        elif num <= second:
            second = num
        else:
            return True
    print(f"final: {first}, {second}")
    return False


def lengthOfLIS(nums, k):
    # 一种更通用的解法，LIS
    if not nums:
        return 0

    def binary_search(tails, key):
        l, r = 0, len(tails) - 1
        while l <= r:
            mid = (l + r) // 2
            if tails[mid] == key:
                return mid
            elif tails[mid] < key:
                l = mid + 1
            else:
                r = mid - 1
        return l

    tails = [nums[0]]
    for num in nums[1:]:
        print(f"tail: {tails}")
        if num > tails[-1]:
            tails.append(num)
        else:
            idx = binary_search(tails, num)
            tails[idx] = num

    print(tails)
    return len(tails) == k


if __name__ == "__main__":
    # [20,100,10,12,5,13]
    print(increasingTriplet2([4, 2, 4, 9]))
    print(increasingTriplet2([20, 100, 10, 12, 5, 13]))
    print(increasingTriplet2([1, 5, 0, 4, 1, 3]))
    print(increasingTriplet2([2, 4, -2, -3]))
    print(increasingTriplet2([2, 4, 1]))
    print(increasingTriplet2([2, 3]))

    print(lengthOfLIS([20, 100, 10, 12, 5, 13], 3))
    print(lengthOfLIS([2, 4, -2, -3], 3))
