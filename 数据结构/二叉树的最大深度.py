"""
Author: ByronVon
Date: 2023-08-10 13:43:34
FilePath: /leetcode/数据结构/二叉树的最大深度.py
Description: https://leetcode.cn/problems/maximum-depth-of-binary-tree/?envType=study-plan-v2&envId=leetcode-75
"""

from utils import *


def maxDepth(root):
    """
    树的遍历方式总体分为两类：深度优先搜索（DFS）、广度优先搜索（BFS）。

    常见 DFS ： 先序遍历、中序遍历、后序遍历。
    常见 BFS ： 层序遍历（即按层遍历）。
    """
    # 先遍历左子树的深度(maxDepth(root.left))
    # 再遍历右子树的深度(maxDepth(root.right))
    # 返回max(maxDepth(root.left), maxDepth(root.right))+1
    if not root:
        return 0
    return max(maxDepth(root.left), maxDepth(root.right)) + 1


def buildTree(roots):
    nodes = [TreeNode(r) for r in roots]

    for i in range(len(nodes)):
        if 2 * i + 1 < len(nodes):
            nodes[i].left = nodes[2 * i + 1]
        if 2 * i + 2 < len(nodes):
            nodes[i].right = nodes[2 * i + 2]
    return nodes


if __name__ == "__main__":
    roots = [3, 9, 20, None, None, 15, 7]
    nodes = buildTree(roots)
    # print(nodes)
    for node in nodes:
        if node.val is not None:
            print(node.val, node.left, node.right)

    print(maxDepth(nodes))
