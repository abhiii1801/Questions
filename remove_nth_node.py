#https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        temp = head
        while temp is not None:
            temp = temp.next
            length += 1

        if n == length:
            return head.next

        remove = (length - n)-1
        current = head
        for i in range(remove):
            current = current.next
        
        if current.next:
            current.next = current.next.next

        return head

