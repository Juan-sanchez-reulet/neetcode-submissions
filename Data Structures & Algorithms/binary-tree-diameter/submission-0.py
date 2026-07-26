# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = [0]  # Usamos una lista de 1 elemento para guardar el récord

        def dfs(node):
            if not node:
                return 0
            
            # 1. Calculamos alturas de cada lado
            izq = dfs(node.left)
            der = dfs(node.right)
            
            # 2. Actualizamos la suma máxima (diámetro)
            res[0] = max(res[0], izq + der)
            
            # 3. Devolvemos la altura al padre
            return 1 + max(izq, der)

        dfs(root)
        return res[0]