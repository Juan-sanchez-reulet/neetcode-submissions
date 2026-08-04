class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        two_back = 0  # Coste mínimo para llegar a i-2
        one_back = 0  # Coste mínimo para llegar a i-1
        
        for i in range(2, len(cost) + 1):
            current = min(one_back + cost[i - 1], two_back + cost[i - 2])
            two_back = one_back
            one_back = current
            
        return one_back