"""
Author: ByronVon
Date: 2023-08-23 14:04:45
FilePath: /leetcode/数据结构/二叉树的右视图.py
Description: 
"""
from utils import *


def rightSideView(root):
    # 获取二叉树从顶部到底部的顺序
    # 返回右侧能看到的节点值
    # 广度优先遍历
    if not root:
        return []

    queue = [root]
    res = []
    while queue:
        level_size = len(queue)
        print([q.val for q in queue])
        for i in range(level_size):
            curr = queue.pop(0)
            # 只记录最后一个节点的值
            if i == level_size - 1:
                res.append(curr.val)
            # 不能只记录curr.right,最后的一个节点也许在左子树出现
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
    print(f"**{res}**")
    return res


def rightSideView2(root):
    if not root:
        return []

    queue = [root, None]  # 使用None作为层的分隔
    res = []
    last_node_val = root.val

    while queue:
        curr = queue.pop(0)

        if curr:
            last_node_val = curr.val
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
        else:
            res.append(last_node_val)
            if queue:  # 检查是否还有其他节点需要处理
                queue.append(None)
    print(res)
    return res


def rightSideView3(root):
    def dfs(node, depth):
        if not node:
            return
        # 每次我们首次访问一个新的深度，即在右边看到的第一个节点
        if depth == len(view):
            view.append(node.val)
        dfs(node.right, depth + 1)
        dfs(node.left, depth + 1)

    view = []
    dfs(root, 0)
    print(view)
    return view


def bfs(root):
    if not root:
        return []
    queue = [root]
    res = []
    while queue:
        curr = queue.pop(0)
        res.append(curr.val)
        if curr.left:
            queue.append(curr.left)
        if curr.right:
            queue.append(curr.right)
    return res


if __name__ == "__main__":
    tree1 = build_tree([1, 2, 3, None, 5, None, 4])
    tree2 = build_tree([1, None, 3])
    tree3 = build_tree([1, 2, 3, None, 5, 6, 4])
    tree4 = build_tree([1, 2, 3, None, 5])

    rightSideView3(tree1)
    rightSideView3(tree2)
    rightSideView3(tree3)
    rightSideView3(tree4)
    # print(bfs(tree3))
    # print(bfs(tree4))
