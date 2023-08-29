"""
Author: ByronVon
Date: 2023-08-15 16:23:52
FilePath: /leetcode/数据结构/删除链表的中间节点.py
Description: 
"""
from utils import *


def deleteMiddle(head):
    # delete中间节点，确定中间节点的位置
    # 快慢指针经典习题
    # 使用两个指针，一个快指针和一个慢指针。快指针一次移动两个节点，而慢指针一次移动一个节点。
    # 当快指针到达链表末尾时，慢指针正好在中间节点。但为了删除中间节点，我们需要找到中间节点的前一个节点。因此，当快指针开始时，慢指针应该从头节点的前一个位置开始（可以使用一个哑节点）。
    # 删除慢指针指向的下一个节点（即中间节点）。
    if not head or not head.next:
        return None
    dummy = ListNode(0)
    dummy.next = head
    slow, fast = dummy, head  # 分别指向不同的节点，为了删除中间节点，因此考虑slow为空节点
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    # 删除中间节点，此时slow位于中间节点的上一个节点
    slow.next = slow.next.next

    return dummy.next


if __name__ == "__main__":
    # head = [1, 3, 4, 7, 1, 2, 6]
    # head = [1, 2, 3, 4]
    head = [1, 2]

    linkedlist = build_list(head)

    print(deleteMiddle(linkedlist, len(head) // 2))
