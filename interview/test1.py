"""
Author: ByronVon
Date: 2023-08-09 16:02:34
FilePath: /leetcode/面试/test1.py
Description: 
"""

# 输出LIST中的偶数平方
import os


def fun1(ls):
    return [i**2 for i in ls if i % 2 == 0]


def fun2(fp):
    # 读取jsonlines文件
    # 用seek的方式改一下
    with open(fp) as f:
        lines = f.readlines()
    for line in lines:
        yield line


if __name__ == "__main__":
    # print(fun1(range(6)))
    fun2("./demo.jl")
