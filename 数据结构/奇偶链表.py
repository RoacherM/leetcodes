"""
Author: ByronVon
Date: 2023-08-15 18:28:24
FilePath: /leetcode/数据结构/奇偶链表.py
Description: 
"""

from utils import *


def oddEvenList(head):
    ## 将奇数节点和偶数节点分别组合在一起，并返回结果
    ## 第一个节点的index为奇数；第二个为偶数
    ## 在O(1)的额外空间复杂度和O(1)的时间复杂度下解决该问题
    ## [1,2,3,4,5]->[1,3,5,2,4]
    ## [2,1,3,5,6,4,7]->[2,3,6,7,1,5,4]
    # odd = ListNode()  # 奇数节点
    # even = ListNode()  # 偶数节点
    odd = head
    even = head.next
    evenHead = even  # 保存偶数链表的头部
    while even and even.next:
        # 修改当前节点的指向
        print(odd.val, even.val)
        # 更新当前节点
        odd.next = even.next
        odd = odd.next

        even.next = odd.next
        even = even.next

    odd.next = evenHead
    print(traverse(head))
    return head  #


if __name__ == "__main__":
    head1 = [1, 2, 3, 4, 5]
    head2 = [2, 1, 3, 5, 6, 4, 7]
    oddEvenList(build_list(head1))
    oddEvenList(build_list(head2))

    print(traverse(build_list(head1)))
    print(traverse(build_list(head2)))
