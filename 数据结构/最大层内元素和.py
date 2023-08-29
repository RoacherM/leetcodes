"""
Author: ByronVon
Date: 2023-08-23 14:59:41
FilePath: /leetcode/数据结构/最大层内元素和.py
Description: 
"""
from collections import deque

from utils import *


def maxLevelSum(root):
    # 给你一颗二叉树，返回每一层元素和最大的层号，如果存在多层，则返回第一个
    # 层数从1开始
    if not root:
        return None

    ans = []
    total = float("-inf")
    level = 1
    queue = [root]
    while queue:
        level_size = len(queue)
        level_sums = 0
        for i in range(level_size):
            curr = queue.pop(0)
            level_sums += curr.val
            if i == level_size - 1:
                print(f"level, sums: {level}, {level_sums}")
                if level_sums > total:
                    total = level_sums
                    ans = level
                level += 1
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
    return ans


def maxLevelSum2(root):
    # 优化下
    # 使用deque取值，而不是list的pop
    if not root:
        return None
    max_sum = float("-inf")
    max_level = 0

    level = 1
    queue = deque([root])

    while queue:
        level_size = len(queue)
        level_sums = 0
        for i in range(level_size):
            curr = queue.popleft()  # O(1)复杂度
            level_sums += curr.val
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
        # 更新最大和 与 对应的层号
        if level_sums > max_sum:
            max_sum = level_sums
            max_level = level
        level += 1
    return max_level


def maxLevelSum3(root):
    if not root:
        return 0

    max_sum = float("-inf")
    max_level = 0

    current_level = 1  # 定义初始层
    level_sum = 0  # 定义初始层的和
    queue = deque([(root, current_level)])  # 定义初始队列

    while queue:
        curr, level = queue.popleft()

        if level > current_level:
            # 如果进入了新的层级，更新层数并重置当前层的和
            if max_sum < level_sum:
                max_sum = level_sum
                max_level = current_level
            level_sum = 0
            current_level = level

        level_sum += curr.val

        if curr.left:
            queue.append((curr.left, level + 1))
        if curr.right:
            queue.append((curr.right, level + 1))

    # 最后需要再次检查一下最后一层的和，因为在循环结束后可能没有检查
    if max_sum < level_sum:
        return current_level
    else:
        return max_level


def maxLevelSum4(root):
    # 使用dfs实现+字典实现
    if not root:
        return None

    level_dict = {}

    def dfs(root, level):
        if not root:
            return
        # 存储每一层的和
        if level not in level_dict:
            level_dict[level] = 0

        level_dict[level] += root.val
        dfs(root.left, level + 1)
        dfs(root.right, level + 1)

    dfs(root, 1)  # 从层1开始
    max_level = max(level_dict, key=level_dict.get)
    return max_level


if __name__ == "__main__":
    tree1 = build_tree([1, 7, 0, 7, -8, None, None])
    tree2 = build_tree([989, None, 10250, 98963, -89388, None, None, None, -32127])
    print(maxLevelSum4(tree1))
    print(maxLevelSum4(tree2))
