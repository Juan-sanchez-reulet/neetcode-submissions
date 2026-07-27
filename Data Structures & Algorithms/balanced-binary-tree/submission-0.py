# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(node):
            if not node:
                return 0  # Caso base: la altura de un nodo nulo es 0
            
            izq = dfs(node.left)
            der = dfs(node.right)
            
            # 1. Si algún hijo ya estaba desbalanceado (-1) 
            # O si el nodo actual se desbalancea (> 1)
            if izq == -1 or der == -1 or abs(izq - der) > 1:
                return -1  # Propagamos el error hacia arriba
            
            # 2. Si todo está en orden, devolvemos la altura normal
            return 1 + max(izq, der)

        # Si el resultado final no es -1, significa que todo el árbol está balanceado
        return dfs(root) != -1