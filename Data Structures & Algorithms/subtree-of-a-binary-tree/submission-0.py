# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # 1. Tu función isSameTree (corregida sin variables innecesarias)
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q or p.val != q.val:
            return False
        
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

    # 2. La función principal
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # Caso base: si el árbol principal se vacía y no encontramos subRoot
        if not root:
            return False
        
        # Paso 1: ¿Es el árbol actual idéntico a subRoot?
        if self.isSameTree(root, subRoot):
            return True
        
        # Paso 2: Si no lo es, buscamos recursivamente en la izquierda O en la derecha
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

