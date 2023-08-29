"""
Author: ByronVon
Date: 2023-08-11 10:36:59
FilePath: /leetcode/数据结构/叶子相似的树.py
Description: https://leetcode.cn/problems/leaf-similar-trees/?envType=study-plan-v2&envId=leetcode-75
"""

from utils import *


def find_leaf_by_inorder(root):
    """
    用中序遍历的方式，依次获得左右节点
    """
    res = []

    def inorder(root):
        if not root:
            return None
        inorder(root.left)
        inorder(root.right)
        if not root.left and not root.right:
            res.append(root.val)

    inorder(root)
    return res


def leafSimilar(root1, root2):
    # 依次遍历树节点，从左到右，将叶子节点加入到list中
    # 比较两个list是否一致即可

    leef1 = find_leaf_by_inorder(root1)
    leef2 = find_leaf_by_inorder(root2)
    print(leef1, leef2)
    # if leef1 == leef2:
    #     return True
    # return False
    return leef1 == leef2


if __name__ == "__main__":
    list1 = [3, 5, 1, 6, 2, 9, 8, None, None, 7, 4]
    list2 = [3, 5, 1, 6, 7, 4, 2, None, None, None, None, None, None, 9, 8]

    list3 = [1, 2, 3]
    list4 = [1, 3, 2]

    tree1 = build_tree(list1)
    tree2 = build_tree(list2)

    tree3 = build_tree(list3)
    tree4 = build_tree(list4)

    print(leafSimilar(tree1, tree2))

    print(leafSimilar(tree3, tree4))
