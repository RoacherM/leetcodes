"""
Author: ByronVon
Date: 2023-08-15 22:49:46
FilePath: /leetcode/动态规划/泰波那契数.py
Description: 
"""


def tribonacci(n):
    # T[0]=0, T[1]=1, T[2]=1
    # T[n+3] = T[n+2] + T[n+1] + T[n]
    # 第N个位置的结果只和前三个值有关，因此，每次只保留这三位的结果即可
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1

    i, j, k = 0, 1, 1

    for _ in range(3, n + 1):
        # print(f"ijk: {i}:{j}:{k}")
        l = i + j + k
        i, j, k = j, k, l
    return l


if __name__ == "__main__":
    print(tribonacci(4))
    print(tribonacci(25))
