class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        
        while n > 0:
            # 1. Si el último bit es 1, suma 1; si es 0, suma 0.
            count += n & 1
            
            # 2. Desplazamos todos los bits un paso a la derecha
            n = n >> 1
            
        return count