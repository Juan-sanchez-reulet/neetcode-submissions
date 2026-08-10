class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        
        for _ in range(32):
            # 1. Desplazamos res a la izquierda para hacer hueco
            res = res << 1
            
            # 2. Extraemos el último bit de n y se lo añadimos a res
            res = res | (n & 1)
            
            # 3. Descartamos el último bit de n
            n = n >> 1
            
        return res