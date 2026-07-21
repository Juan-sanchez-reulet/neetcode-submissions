# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return
        
        # --- PASO 1: Buscar la mitad ---
        lento, rapido = head, head.next
        while rapido and rapido.next:
            lento = lento.next
            rapido = rapido.next.next
            
        # lento.next es el inicio de la segunda mitad
        segunda = lento.next
        lento.next = None  # Cortamos la lista en dos
        
        # --- PASO 2: Invertir la segunda mitad ---
        prev = None
        curr = segunda
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        segunda = prev  # 'prev' es la cabeza de la segunda mitad invertida
        
        # --- PASO 3: Entrelazar las dos listas ---
        primera = head
        while segunda:
            tmp1, tmp2 = primera.next, segunda.next
            
            primera.next = segunda   # Enganchamos el nodo de la 2ª mitad
            segunda.next = tmp1      # Enganchamos el resto de la 1ª mitad
            
            primera = tmp1           # Avanzamos en la 1ª mitad
            segunda = tmp2
            