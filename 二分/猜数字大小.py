"""
Author: ByronVon
Date: 2023-08-11 14:53:44
FilePath: /leetcode/二分/猜数字大小.py
Description: https://leetcode.cn/problems/guess-number-higher-or-lower/?envType=study-plan-v2&envId=leetcode-75
"""


def guessNumber(n, pick):
    # 事先有一个guess函数，可以返回下面的结果
    # -1: 选的数字比猜的小，即pick < num
    # 0: 一样，即pick == num
    # +1: 选的数字比猜的大，即pick > num

    # print(f"{n}--{pick}")
    begin, end = 1, n
    mid = (begin + end) // 2
    res = guess(pick, mid)

    while res != 0:
        # print(begin, end, mid, pick)
        if res == 1:
            begin, end = mid, end
            mid = (begin + end) // 2 + 1
        else:
            begin, end = begin, mid
            mid = (begin + end) // 2
        res = guess(pick, mid)
    return mid


def guess(pick, num):
    if pick > num:
        return 1
    elif pick < num:
        return -1
    else:
        return 0


if __name__ == "__main__":
    num = 20
    for i in range(1, num + 1):
        # print(f"{i}")
        res = guessNumber(num, i)
        print(f"num: {num}, pick: {i}, res: {res}")
