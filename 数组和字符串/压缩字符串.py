"""
Author: ByronVon
Date: 2023-08-14 11:36:33
FilePath: /leetcode/数组和字符串/压缩字符串.py
Description:
"""


def compressString(chars):
    """
    从一个空字符串 s 开始。对于 chars 中的每组 连续重复字符 ：
    如果这一组长度为 1 ，则将字符追加到 s 中。
    否则，需要向 s 追加字符，后跟这一组的长度。
    压缩后得到的字符串 s 不应该直接返回 ，需要转储到字符数组 chars 中。
    需要注意的是，如果组长度为 10 或 10 以上，则在 chars 数组中会被拆分为多个字符。
    请在 修改完输入数组后 ，返回该数组的新长度。
    你必须设计并实现一个只使用常量额外空间的算法来解决此问题。
    # chars[i] 可以是小写英文字母、大写英文字母、数字或符号
    """
    # ['a', 'a', 'b', 'b', 'c']->['a', 2, 'b', 2, 'c']
    # ['a']->['a']
    # ['a'] * 12 -> ['a', '1', '2']
    res = []
    tmp = ""  # 记录每个字符的起始位置, 然后记录j-i为每个字符连续出现的次数
    for i in range(len(chars)):
        if not tmp:
            tmp += chars[i]
        else:
            if chars[i] != tmp[-1]:
                res.append(tmp[-1])
                res.append(len(tmp))  # 如果是1则不加，如果超过10则按位加
                tmp = chars[i]
            else:
                tmp += chars[i]
    if tmp:
        res.append(tmp[-1])
        res.append(len(tmp))
    print(res)
    return res


def compressString2(chars):
    ans = []
    chr, i = chars[0], 0
    for j in range(1, len(chars)):
        # 如果不相等，则将chr加入 到ans中，并记录位置
        if chars[j] != chr:
            ans.append(chr)
            ans.extend(comp(j - i))
            chr = chars[j]
            i = j
    if chr:
        ans.append(chr)
        ans.extend(comp(len(chars) - i))
    print(ans)
    return len(ans)


def compressString3(chars):
    # 需要修改原chars，即将某些连续字符串的第二个字母替换为数字，
    # 用双指针的方式解决，左指针指向当前的字符，右指针遍历字符串长度，
    # 当左右指针不相等时，将左指针+1位置变为长度，更新左指针
    l = 0  # l记录字符串开始位置, r记录字符串写的位置
    x = 0  # x记录字符串长度
    for r in range(len(chars)):
        if chars[r] != chars[l]:
            print(chars[l:r], f"{l}-{r}")  #
            # gap = l - r
            num = split_number(r - l)
            # print(num)
            x = x + 1 + len(num)
            for n in range(len(num)):
                l += 1
                chars[l] = num[n]
            l = r

    # print(chars[l:])
    # 查漏补缺一下
    num = split_number(len(chars) - l)
    for n in range(len(num)):
        l += 1
        chars[l] = num[n]
    x = x + 1 + len(num)
    # 需要将剩下的内容更新到chars中
    print("#", chars, x)
    print("*" * 100)


def compressString4(chars):
    # 需要修改原chars，即将某些连续字符串的第二个字母替换为数字，如果重复的次数>10则占多个位置
    # 用双指针的方式解决，左指针指向当前的字符，右指针遍历字符串长度，
    # 当左右指针不相等时，将左指针+1位置变为长度，更新左指针
    l, r = 0, 0  # l记录字符串开始位置, r记录字符串写的位置, while控制i更灵活跳转
    x = 0  # x记录字符串长度
    while l < len(chars):  # 双指针的时候一般用while比较合适，跳转更灵活
        print(chars, f"char: {l}->{r}")
        if r == len(chars) or chars[r] != chars[l]:
            # 如果不相等，则更新chars
            num = split_number(r - l)
            x = x + 1 + len(num)
            # 写数组的意思是修改chars[l:l+num]的结果
            for n in num:
                l += 1  # 此时逐步更新l
                chars[l] = n
            # 更新当前的char，修改了
            l = r  # 跳转到最新的位置
        r += 1
    print(chars, x)
    return x


def compressString5(chars):
    # 需要修改原chars，即将某些连续字符串的第二个字母替换为数字，如果重复的次数>10则占多个位置
    # 用双指针的方式解决，write为写字符的位置，read为当前字符的位置
    # 每次从write处依次写入字符和对应长度即可
    # left为字符串最左端的位置，num=read-left+1
    write = left = 0  # write的长度也为压缩后的长度
    for read in range(len(chars)):
        # 当read=len-1或者chars[read]!=chars[read+1]时，到达连续字符串的右端
        if read == len(chars) - 1 or chars[read] != chars[read + 1]:
            # print(chars[write], chars[read])
            chars[write] = chars[read]  # 先在write的位置写入当前字符
            write += 1  # 更新写字符的位置
            num = split_number(read - left + 1)
            # print(num)
            for n in num:
                chars[write] = n  # 依次更新write位置数字
                write += 1
            # 更新left的位置
            left = read + 1
    print(chars, write)


def split_number(num):
    if num > 1:
        return list(str(num))
    return []


class Solution:
    def compress(self, chars):
        # 反转字符串
        def reverse(left, right) -> None:
            while left < right:
                chars[left], chars[right] = chars[right], chars[left]
                left += 1
                right -= 1

        n = len(chars)
        write = left = 0
        for read in range(n):
            if read == n - 1 or chars[read] != chars[read + 1]:
                chars[write] = chars[read]
                write += 1
                num = read - left + 1
                if num > 1:
                    anchor = write
                    while num > 0:
                        chars[write] = str(num % 10)
                        write += 1
                        num //= 10
                    reverse(anchor, write - 1)
                left = read + 1
        print(chars)
        return write


def comp(num):
    if num == 1:
        return []
    elif num > 1 and num < 10:
        return [str(num)]
    else:
        return list(str(num))


if __name__ == "__main__":
    compressString5(["a", "a", "b", "b", "c", "c", "c"])
    compressString5(["a"])
    compressString5(["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"])
    compressString5(["a", "v", "v", 10, 10, 12, 12, 9])
    compressString5(["a", "n", "c"])
    compressString5(["a", "a", "a", "b", "b", "a", "a"])
    compressString5(["a", "a", "a", "c", "b", "b"])
    # s = Solution()
    # s.compress(["a", "a", "b", "b", "c", "c", "c"])
    # s.compress(["a"])
    # s.compress(["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"])
    # s.compress(["a", "v", "v", 10, 10, 12, 12, 9])
