"""
Author: ByronVon
Date: 2023-08-11 16:02:44
FilePath: /leetcode/数据结构/删除二叉搜索树中的节点.py
Description: https://leetcode.cn/problems/delete-node-in-a-bst/?envType=study-plan-v2&envId=leetcode-75
"""


from turtle import right
from utils import *

# 二叉搜索树有以下性质：

# 左子树的所有节点（如果有）的值均小于当前节点的值；
# 右子树的所有节点（如果有）的值均大于当前节点的值；
# 左子树和右子树均为二叉搜索树。


def deleteNode(root, key):
    # 给定一个二叉搜索树的根节点 root 和一个值 key，
    # 删除二叉搜索树中的 key 对应的节点，
    # 并保证二叉搜索树的性质不变。
    # 返回二叉搜索树（有可能被更新）的根节点的引用。
    # 更新的方式
    ## 先尝试用BFS找到满足条件的node,然后更新该node节点

    if not root:
        return None

    if root.val > key:  # 如果root的值比key大，则从左子树找
        root.left = deleteNode(root.left, key)
    elif root.val < key:  # 如果root的值比key小，则从右子树找
        root.right = deleteNode(root.right, key)
    # 开始删除node
    elif root.left is None or root.right is None:  # 如果其中一个为None，则直接上移动
        root = root.left if root.left else root.right
    else:
        successor = root.right  # 为保证有序性，因此只能选右子树
        while successor.left:
            successor = successor.left  # 将原右子树的节点变为现在的右子树
        successor.right = deleteNode(root.right, successor.val)  # 删除最小的左叶节点
        successor.left = root.left  # 将原来的左子树节点变为现在的左子树
        return successor
    return root


if __name__ == "__main__":
    tree1 = build_tree([5, 3, 6, 2, 4, None, 7])

    tree1_ = deleteNode(tree1, 3)
    # tree2_ = deleteNode(tree1, 4)

    print(preorder(tree1_))
    # print(preorder(tree2_))
