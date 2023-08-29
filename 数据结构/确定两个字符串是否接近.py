"""
Author: ByronVon
Date: 2023-08-15 12:42:01
FilePath: /leetcode/数据结构/确定两个字符串是否接近.py
Description: 
"""

# 如果可以使用以下操作从一个字符串得到另一个字符串，则认为两个字符串 接近 ：

# 操作 1：交换任意两个 现有 字符。
# 例如，abcde -> aecdb
# 操作 2：将一个 现有 字符的每次出现转换为另一个 现有 字符，并对另一个字符执行相同的操作。
# 例如，aacabb -> bbcbaa（所有 a 转化为 b ，而所有的 b 转换为 a ）
# 你可以根据需要对任意一个字符串多次使用这两种操作。

# 给你两个字符串，word1 和 word2 。如果 word1 和 word2 接近 ，就返回 true ；否则，返回 false 。


from collections import Counter


def closeStrings(word1, word2):
    # 思路
    # 1、字符频率：两个close的字符串应该具有相同的字符集和字符频率
    # 2、字符集合：两个close的字符集应该相同
    # 3、字符频率分布：字符集相同，字符频率也必须相同的字符串才能close
    # 4、如果满足上述条件，一定可以通过一定的操作得到

    maps1 = dict(Counter(word1))
    maps2 = dict(Counter(word2))

    # 如果字符集合不一样，则不接近
    if sorted(maps1.keys()) != sorted(maps2.keys()):
        return False
    # 如果字符集合一致，但字符
    if sorted(maps1.values()) != sorted(maps2.values()):
        return False
    return True


if __name__ == "__main__":
    print(closeStrings("abcde", "aecdb"))
    print(closeStrings("a", "aa"))
    print(closeStrings("cabbba", "abbccc"))
    print(closeStrings("cabbba", "aabbss"))
