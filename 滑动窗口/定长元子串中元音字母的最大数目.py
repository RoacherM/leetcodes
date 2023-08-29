"""
Author: ByronVon
Date: 2023-08-15 00:34:38
FilePath: /leetcode/滑动窗口/定长元子串中元音字母的最大数目.py
Description: 
"""


def maxVowels(s, k):
    # 给你字符串 s 和整数 k
    # 请返回字符串 s 中长度为 k 的单个子字符串中可能包含的最大元音字母数。
    # 英文中的 元音字母 为（a, e, i, o, u）。
    # 先计算当前窗口中的元音字母个数，然后根据s[i+k], s[i-1]，调整窗口中元音个数
    cur = sum([isVowels(_) for _ in s[:k]])
    ans = cur
    for i in range(1, len(s) - k + 1):
        if isVowels(s[i - 1]):
            cur -= 1
        if isVowels(s[i + k - 1]):
            cur += 1
        # print(s[i : i + k], cur)
        ans = max(ans, cur)
    return ans


def isVowels(s):
    if s in ("a", "e", "i", "o", "u"):
        return 1
    return 0


if __name__ == "__main__":
    print(maxVowels("abciiidefooo", 3))
    print(maxVowels("aeiou", 2))
    print(maxVowels("leetcode", 3))
    print(maxVowels("tryhard", 4))
    print(maxVowels("rhythms", 4))
    print(maxVowels("a" * 10, 10))
    print(maxVowels("a", 1))
