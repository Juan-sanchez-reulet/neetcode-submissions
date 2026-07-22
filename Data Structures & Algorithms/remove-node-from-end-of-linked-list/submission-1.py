# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)  # Nodo falso apuntando a la cabeza
        left = dummy
        right = head

        for _ in range(n):
            right = right.next

        while right:
            left = left.next
            right = right.next

        # 3. 'left' está justo antes del nodo a borrar
        left.next = left.next.next

        # Retornamos la cabeza real (que puede haber cambiado)
        return dummy.next