"""
Author: ByronVon
Date: 2023-08-17 10:49:27
FilePath: /leetcode/数据结构/统计二叉树中好节点的数目.py
Description: 
"""

from utils import *


# def goodNodes(root):
# problem: 只保留了最大值，而未检查祖先节点
#     if not root:
#         return None
#     # val = root.val
#     ans = []

#     def dfs(root):
#         if not root:
#             return
#         curr = root.val
#         if not ans:
#             ans.append(curr)
#         elif curr >= ans[-1]:
#             ans.append(curr)
#         dfs(root.left)
#         dfs(root.right)

#     dfs(root)
#     print(ans)


def goodNodes(root):
    if not root:
        return 0
    # 记录节点的值
    count = 0

    def dfs(node, curr_max):
        # 需要在函数内部修改外部函数的局部变量
        nonlocal count

        if not node:
            return 0

        if node.val >= curr_max:
            count += 1
            curr_max = node.val
        dfs(node.left, curr_max)
        dfs(node.right, curr_max)

    dfs(root, root.val)

    return count


def goodNodes2(root):
    if not root:
        return []

    ans = []

    def dfs(node, curr_max):
        if not node:
            return []

        if node.val >= curr_max:
            ans.append(node.val)
            curr_max = node.val

        dfs(node.left, curr_max)
        dfs(node.right, curr_max)

    dfs(root, root.val)

    return ans


def goodNodes3(root):
    if not root:
        return 0

    count = 0
    # curr_max = [root.val]  # 使用一个列表来保存当前的最大值
    curr_max = root.val

    def dfs(node):
        nonlocal count, curr_max

        if not node:
            return 0

        if node.val >= curr_max:
            count += 1
            prev_max = curr_max  # 先保存下祖先节点
            curr_max = node.val
            dfs(node.left)  # 检查完左子树的后，
            dfs(node.right)  #
            curr_max = prev_max  # 回溯
        else:
            dfs(node.left)
            dfs(node.right)

    dfs(root)
    return count


if __name__ == "__main__":
    root1 = build_tree([3, 1, 4, 3, None, 1, 5])
    root2 = build_tree([3, 3, None, 4, 2])
    root3 = build_tree([1])
    root4 = build_tree([8, 3, 1, None, None, 6, 4, None, None, 7, None, None, 10, None, 14, 13, None, None, None])
    root5 = build_tree([2, None, 4, 10, 8, None, None, 4])
    print(goodNodes3(root1))
    print(goodNodes3(root2))
    print(goodNodes3(root3))
    print(goodNodes3(root4))
    print(goodNodes3(root5))
