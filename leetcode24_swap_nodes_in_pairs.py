'''
给你一个链表，两两交换其中相邻的节点，并返回交换后链表的头节点。你必须在不修改节点内部的值的情况下完成本题（即，只能进行节点交换）。
输入：head = [1,2,3,4]
输出：[2,1,4,3]
示例 2：

输入：head = []
输出：[]
示例 3：

输入：head = [1]
输出：[1]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/swap-nodes-in-pairs
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    # 递归
    def swapPairs(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        one = head
        two = head.next
        three = two.next
        two.next = one
        one.next = self.swapPairs(three)
        return two

    # 迭代

    def swapPairs_iteration(self, head: ListNode) -> ListNode:
        previous = ListNode(0)
        previous.next = head
        temp = previous
        while temp.next is not None and temp.next.next is not None:
            first = temp.next
            second = temp.next.next

            first.next = second.next
            second.next = first
            temp.next = second

            temp = first
        return previous.next
