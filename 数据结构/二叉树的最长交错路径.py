"""
Author: ByronVon
Date: 2023-08-22 22:07:28
FilePath: /leetcode/数据结构/二叉树的最长交错路径.py
Description: 
"""


from utils import *


def longestZigZag(root):
    # 简单的递归
    # 但需要计算left->right和right->left两条路径的结果，然后返回最大的值
    max_len = 0

    def dfs(root, direction, length):
        nonlocal max_len

        if not root:
            return None
        max_len = max(max_len, length)

        if direction == "left":
            dfs(root.right, "right", length + 1)
            dfs(root.left, "left", 1)
        else:
            dfs(root.left, "left", length + 1)
            dfs(root.right, "right", 1)

    dfs(root, "left", 0)
    dfs(root, "right", 0)
    return max_len


if __name__ == "__main__":
    tree1 = build_tree(
        [1, None, 1, 1, 1, None, None, 1, 1, None, 1, None, None, None, 1, None, 1]
    )
    tree2 = build_tree([1, 1, 1, None, 1, None, None, 1, 1, None, 1])
    tree3 = build_tree([1])

    print(longestZigZag(tree1))
    print(longestZigZag(tree2))
    print(longestZigZag(tree3))
