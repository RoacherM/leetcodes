"""
Author: ByronVon
Date: 2023-08-14 22:30:30
FilePath: /leetcode/数据结构/字符串解码.py
Description: 
"""


# def decodeString(s):
#     # 你可以认为原始数据不包含数字，所有的数字只表示重复的次数 k ，
#     # 例如不会出现像 3a 或 2[4] 的输入。
#     # '3[a]2[bc]'->'aaabcbc'
#     # '3[a2[c]]'-->'accaccacc'
#     # 类似四则运算,注意数字的范围时[1:300]
#     ans = []
#     tmp = []
#     for _ in s:
#         if _ != "]":  # 一直入栈
#             tmp.append(_)
#         else:
#             x = []  # 记录字符
#             while tmp:
#                 t = tmp.pop()
#                 if t == "[":  # 最内层的字符串
#                     # 寻找数字
#                     # print("inner x:", x)
#                     x = x * getDigit(tmp)
#                     print(f"substr: {x}")
#                     break  # 最小的部分弹出来，重新堆栈
#                 else:
#                     x.append(t)

#             # print(x)
#             # reverse
#             ans += x[::-1]
#     if tmp:
#         ans += tmp
#     return "".join(ans)


# def getDigit(tmp):
#     # 将[0,0,1]->100
#     num = []
#     while tmp:
#         t = tmp.pop()
#         if t.isdigit():
#             num.append(t)
#         else:
#             tmp.append(t)
#             break
#     return int("".join(num[::-1]))


def decodeString(s):
    # 因为数字为1-300，因此考虑数字一个栈，字母一个栈
    num_stack = []
    str_stack = []
    curr_num = 0
    curr_str = ""
    for ch in s:
        if ch.isdigit():
            # digit_by_digit的构建数字
            curr_num = curr_num * 10 + int(ch)
        elif ch == "[":
            # 将当前的数字和字符推入各自的栈中,并重置
            num_stack.append(curr_num)
            str_stack.append(curr_str)
            curr_num = 0
            curr_str = ""
        elif ch == "]":
            # 开始出栈，根据数字栈中的数字重复当前字符串，并添加到字符串栈顶部的字符串后
            prev_str = str_stack.pop()
            repeat_num = num_stack.pop()
            curr_str = prev_str + curr_str * repeat_num
        else:
            curr_str += ch

    return curr_str


if __name__ == "__main__":
    print(decodeString("3[bc2[ed]]"))
    print(decodeString("2[abc]3[cd]ef"))
    print(decodeString("3[a]2[bc]"))
    print(decodeString("3[a2[c]]"))
    print(decodeString("abc3[cd]xyz"))
    print(decodeString("rsecdfg"))
    print(decodeString("a3[c2[vd3[xy]]]"))
    print(decodeString("100[leetcode]"))
    print(decodeString("3[z]2[2[y]pq4[2[jk]e1[f]]]ef"))
    # tmp = list("cd301")
    # print(getDigit(tmp))
    # print(tmp)
