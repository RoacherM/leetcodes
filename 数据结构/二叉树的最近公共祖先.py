"""
Author: ByronVon
Date: 2023-08-22 22:35:59
FilePath: /leetcode/数据结构/二叉树的最近公共祖先.py
Description: 
"""

from collections import defaultdict

from utils import *


def lowestCommonAncestor(root, p, q):
    # 寻找一个最大深度的公共节点
    # 感觉和最大深度有点关系
    # node.val均不相等，且p!=q
    # 因为时找公共节点，因此，每次都要返回节点，对返回的情况进行分类判断

    if not root:
        return None

    if root.val == p or root.val == q:
        return root.val

    left = lowestCommonAncestor(root.left, p, q)
    right = lowestCommonAncestor(root.right, p, q)
    print(left, right)

    if left and right:
        return root.val
    elif left:
        return left
    elif right:
        return right
    else:
        return None


if __name__ == "__main__":
    tree1 = build_tree([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
    tree2 = build_tree([1, 2])

    # print(lowestCommonAncestor(tree1, 5, 1))

    print(lowestCommonAncestor(tree1, 5, 4))

    # print(lowestCommonAncestor(tree2, 1, 2))
