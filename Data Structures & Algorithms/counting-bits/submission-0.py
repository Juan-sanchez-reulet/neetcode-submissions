class Solution:
    def countBits(self, n: int) -> list[int]:
        # Creamos el array de respuestas de tamaño (n + 1) lleno de ceros
        dp = [0] * (n + 1)
        
        # Llenamos dp desde 1 hasta n
        for i in range(1, n + 1):
            dp[i] = dp[i >> 1] + (i & 1)
            
        return dp