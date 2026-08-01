import heapq

class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        # 1. Invertimos los signos para simular un Max-Heap
        stones = [-s for s in stones]
        heapq.heapify(stones)
        
        # 2. Simulamos mientras haya al menos 2 piedras
        while len(stones) > 1:
            first = -heapq.heappop(stones)   # La más pesada
            second = -heapq.heappop(stones)  # La segunda más pesada
            
            if first != second:
                # La piedra restante se vuelve a meter (negativa)
                heapq.heappush(stones, -(first - second))
                
        # 3. Si queda una piedra la devolvemos positiva, si no, devolvemos 0
        return -stones[0] if stones else 0