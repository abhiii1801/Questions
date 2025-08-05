#https://leetcode.com/problems/middle-of-the-linked-list/description/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         length = 0
#         temp = head
#         while temp:
#             length += 1
#             temp = temp.next
#         for _ in range((length//2)):
#             head = head.next       
#         return head

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        first = head
        second = head
        while second is not None and second.next is not None:
            first = first.next
            second = second.next.next
        
        return first

        
        