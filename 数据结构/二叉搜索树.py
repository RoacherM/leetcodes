"""
Author: ByronVon
Date: 2023-08-11 14:21:15
FilePath: /leetcode/数据结构/二叉搜索树.py
Description: https://leetcode.cn/problems/search-in-a-binary-search-tree/?envType=study-plan-v2&envId=leetcode-75
"""


from utils import *


def searchBST(root, val):
    # 在给定的二叉搜索树中找到节点值等于val的节点，
    # 赶回以改节点为根的子树，不存在则返回None
    # bfs 遍历
    if not root:
        return None

    queue = [root]
    while queue:
        node = queue.pop(0)
        if node.val == val:
            return node
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return None


if __name__ == "__main__":
    tree = build_tree([4, 2, 7, 1, 3])

    rest = searchBST(tree, 10)
    if rest is not None:
        print(rest.val, rest.left, rest.right)
