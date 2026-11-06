# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #1. finding middle part
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        #2. reverse the second half
        prev = None
        curr = slow

    #Keep repeating the loop as long as curr is pointing to a valid node
        while curr:
            #Save the next node in a temporary variable so we don't lose access to the remaining linked list when we reverse the pointer
            next_node = curr.next
            #Change the current node's next pointer to point to the previous node instead of the next node. This is how we reverse the linked list.
            curr.next = prev
            #Move prev forward to the current node because the current node is now part of the reversed list.
            prev = curr
            #Move curr forward to the next node we saved earlier so we can reverse that node next
            curr = next_node

        #3. merge the two halves
        first = head
        second = prev


        while second.next:
            temp1 = first.next
            temp2 = second.next

            first.next = second
            second.next = temp1

            first = temp1
            second = temp2

        