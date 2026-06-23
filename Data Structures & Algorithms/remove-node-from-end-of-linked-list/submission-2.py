class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        curr = head

        while curr:
            length += 1
            curr = curr.next

        index = length - n

        if index == 0:
            return head.next

        curr = head

        for _ in range(index - 1):
            curr = curr.next

        curr = curr.next.next

        return head