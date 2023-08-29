"""
Author: ByronVon
Date: 2023-08-15 19:29:45
FilePath: /leetcode/数据结构/链表最大孪生和.py
Description: 
"""
from utils import *

from collections import deque


def pairSum(head):
    if not head or not head.next:
        return 0

    slow, fast = head, head
    queue = deque()

    max_twin_sum = float("-inf")

    while fast and fast.next:
        queue.appendleft(slow.val)
        slow = slow.next
        fast = fast.next.next

    while slow:
        max_twin_sum = max(max_twin_sum, queue.popleft() + slow.val)
        slow = slow.next

    return max_twin_sum


def pairSum2(head):
    # 快慢指针，slow,fast都从0开始，找到middle
    # 用一个queue记录slow.val
    # 找到middle节点后，继续遍历，然后每次计算slow.val+queue.pop()
    if not head or not head.next:
        return None

    ans = float("-inf")
    slow, fast = head, head

    queue = []
    # 快慢指针，找到中点
    while fast and fast.next:
        queue.append(slow.val)
        slow = slow.next
        fast = fast.next.next

    while slow:
        ans = max(ans, queue.pop() + slow.val)
        slow = slow.next
    print(ans)
    return ans


if __name__ == "__main__":
    pairSum(build_list([4, 2, 2, 3]))
    pairSum(build_list([1, 10000]))
    pairSum(build_list([5, 4, 2, 1]))
