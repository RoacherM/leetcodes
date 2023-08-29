"""
Author: ByronVon
Date: 2023-08-02 17:11:05
FilePath: /leetcode/数组和字符串/交替合并字符串.py
Description: https://leetcode.cn/problems/merge-strings-alternately/?envType=study-plan-v2&envId=leetcode-75
"""

# 将两个字符串交叉合并
# 考虑 string_a = a->b->c, string_b = d->e->f
# 那么合并后的结果就是 adbecf
# 本质是合并链表


def solution1(string_a, string_b):
    # 最简单的思路，就是先对等长度的字串进行交叉遍历，然后补上余下的长度
    if not string_a:
        return string_b
    if not string_b:
        return string_a

    temp = ""
    lens = min(len(string_a), len(string_b))

    for i in range(lens):
        temp += string_a[i]
        temp += string_b[i]

    temp += string_a[lens:]
    temp += string_b[lens:]
    return temp


def solution2(string_a, string_b):
    # 用pop，将每个string视作一个队列，然后每次弹出最上面的元素
    temp = ""
    list_a = list(string_a)
    list_b = list(string_b)

    while list_a and list_b:
        temp += list_a.pop(0)
        temp += list_b.pop(0)

    if list_a:
        temp += "".join(list_a)
    if list_b:
        temp += "".join(list_b)
    return temp


if __name__ == "__main__":
    test_a = ["abc", "ab", "abcd"]
    test_b = ["pqr", "pqrs", "pq"]

    for a, b in zip(test_a, test_b):
        print(solution1(a, b))
