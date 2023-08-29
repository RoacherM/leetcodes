"""
Author: ByronVon
Date: 2023-08-22 20:10:43
FilePath: /leetcode/数据结构/路径总和3.py
Description: 
"""

from collections import defaultdict

from utils import *


def pathSum(root, targetSum):
    # 递归的思路来做
    # 深度优先遍历，先检查当前的根节点，如果当前的根节点大于等于8
    if not root:
        return 0

    ans = 0
    prefixSumCounter = defaultdict(int)
    prefixSumCounter[0] = 1  # 建立前缀和字典

    # root为当前节点，prev为历史节点
    def dfs(root, currSum):
        nonlocal ans

        if not root:
            return
        currSum += root.val

        ans += prefixSumCounter[currSum - targetSum]
        prefixSumCounter[currSum] += 1

        dfs(root.left, currSum)
        dfs(root.right, currSum)

        # backtrace
        prefixSumCounter[currSum] -= 1

    dfs(root, 0)

    return ans


if __name__ == "__main__":
    tree1 = build_tree([10, 5, -3, 3, 2, None, 11, 3, -2, None, 1])
    tree2 = build_tree([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1])

    print(pathSum(tree1, 8))
    print("*" * 20)
    print(pathSum(tree2, 22))
