"""
Author: ByronVon
Date: 2023-08-11 22:28:09
FilePath: /leetcode/数据结构/单调栈.py
Description: https://leetcode.cn/problems/daily-temperatures/?envType=study-plan-v2&envId=leetcode-75
"""


def dailyTemperatures(temperatures):
    # 返回下一个高温天气距离和当前的距离
    # 遍历下即可, 但是时间复杂度较高，需要优化
    rest = [0] * len(temperatures)
    for i in range(len(temperatures)):
        for j in range(i + 1, len(temperatures)):
            if temperatures[j] > temperatures[i]:
                rest[i] = j - i
                break  # 找到之后就停止遍历
    return rest


def dailyTemperatures2(temperatures):
    # 用双指针的方式，进行更灵活的跳转
    # 遇到双循环，可以考虑用双指针进行优化，但并未优化多少，只是变得更灵活而已
    rest = [0] * len(temperatures)
    i, j = 0, 1
    while i < len(temperatures):
        print(i, j, rest)
        if temperatures[i] < temperatures[j]:
            rest[i] = j - i
            i += 1
            j = i + 1
        else:
            j += 1
        if j == len(temperatures):  # 若到头了也没找到，则i+1,j回调
            i += 1
            j = i
    # print(rest)
    return rest


def dailyTemperatures3(temperatures):
    # 用单调栈的方式记录单调数组

    rest = [0] * len(temperatures)
    stack = []
    for i in range(len(temperatures)):
        temperature = temperatures[i]
        # 若不单调，则从尾部开始，依次更新结果
        while stack and temperature > temperatures[stack[-1]]:
            # 更新位置
            prev = stack.pop()
            rest[prev] = i - prev
            print(stack, prev)
        # 依次压栈，存当前的位置信息
        stack.append(i)
    return rest


if __name__ == "__main__":
    print(dailyTemperatures3([73, 74, 75, 71, 69, 72, 76, 73]))
    print(dailyTemperatures3([30, 40, 50, 60]))
    print(dailyTemperatures3([30, 60, 90]))
