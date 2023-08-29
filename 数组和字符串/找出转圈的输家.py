"""
Author: ByronVon
Date: 2023-08-16 10:15:36
FilePath: /leetcode/数组和字符串/找出转圈的输家.py
Description: 
"""


def circularGameLosers(n, k):
    # n个朋友围成一个圈，按照1-n进行编号
    # 每个人接球后向顺时针k方向的朋友传递
    # 在第 i 轮中持有球的那位朋友需要将球传递给距离他顺时针方向 i * k 步的朋友。
    # 当某个朋友第 2 次接到球时，游戏结束。
    # 在整场游戏中没有接到过球的朋友是 输家 。
    # 给你参与游戏的朋友数量 n 和一个整数 k ，请按升序排列返回包含所有输家编号的数组 answer 作为答案。
    # 第i轮的位置为 (i+i*k)%n
    turn = 1
    curr = 1
    used = set()
    while True:
        # print(curr, turn)
        if curr not in used:
            used.add(curr)
            # 添加修改curr的位置
            curr = (curr + turn * k) % n
            curr = n if not curr else curr  # 被整除时需要修改下
            turn += 1
        else:
            break
    print(used)
    print([i + 1 for i in range(n)])
    return [i + 1 for i in range(n) if i + 1 not in used]


if __name__ == "__main__":
    print(circularGameLosers(4, 4))
    print(circularGameLosers(2, 1))
