import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.minHeap = nums
        
        # 1. Transformamos la lista inicial en un Min-Heap
        heapq.heapify(self.minHeap)
        
        # 2. Si hay más de k elementos, descartamos los más pequeños
        # hasta quedarnos SOLO con los k más grandes.
        while len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        # 1. Añadimos el nuevo elemento al heap
        heapq.heappush(self.minHeap, val)
        
        # 2. Si al añadirlo superamos el tamaño k, eliminamos el menor de todos
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
            
        # 3. El elemento más pequeño de los k guardados es el k-ésimo mayor global
        return self.minHeap[0]
