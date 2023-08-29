"""
Author: ByronVon
Date: 2023-08-10 13:18:39
FilePath: /leetcode/数据结构/反转链表.py
Description: https://leetcode.cn/problems/reverse-linked-list/?envType=study-plan-v2&envId=leetcode-75
"""


from utils import *


def reverseList(head):
    # 给定一个单链表，请反转链表，并返回反转后的链表
    # 遍历节点：while head.next:
    prev = None
    curr = head
    while curr:
        tmp = curr.next  # 记录下一个位置
        curr.next = prev  # 修改next的指向
        prev = curr  # 更新prev
        curr = tmp  # 更新curr
    return prev


if __name__ == "__main__":
    head = [1, 2, 3, 4, 5]
    lists = ListNode(head[0])
