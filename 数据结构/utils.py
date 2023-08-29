"""
Author: ByronVon
Date: 2023-08-11 14:21:46
FilePath: /leetcode/数据结构/utils.py
Description: 基础数据结构
"""


class ListNode:
    def __init__(self, val=0, next=None) -> None:
        self.val = val
        self.next = next


class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right


def build_list(lst):
    # 遍历链表
    dummy = ListNode()
    curr = dummy
    for l in lst:
        curr.next = ListNode(l)
        curr = curr.next
    return dummy.next


def build_tree(lst):
    # BFS实现二叉树的遍历
    if not lst:
        return None
    root = TreeNode(lst[0])
    node_queue = [root]
    i = 1
    while i < len(lst):
        node = node_queue.pop(0)
        # print(f"node: {node.val}, {lst[i]}")
        if lst[i]:
            node.left = TreeNode(lst[i])
            node_queue.append(node.left)
        i += 1
        if i >= len(lst):
            break
        if lst[i]:
            node.right = TreeNode(lst[i])
            node_queue.append(node.right)
        i += 1
    return root


def preorder(root):
    # 前序遍历二叉树: 根节点->左子树->右子树
    if not root:
        print("null")
        return None
    print(root.val)
    preorder(root.left)
    preorder(root.right)


def inorder(root):
    # 中序遍历二叉树: 左子树->根节点->右子树
    if not root:
        print("null")
        return None
    inorder(root.left)
    print(root.val)
    inorder(root.right)


def postorder(root):
    # 后序遍历二叉树: 左子树->右子树->根节点
    if not root:
        print("null")
        return None
    postorder(root.left)
    postorder(root.right)
    print(root.val)


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


def traverse(head):
    if not head:
        return []
    res = []
    curr = head
    while curr:
        res.append(curr.val)
        curr = curr.next
    return res
