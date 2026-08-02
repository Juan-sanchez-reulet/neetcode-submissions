class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        
        # one representa el escalón anterior (n-1)
        # two representa el escalón previo al anterior (n-2)
        one, two = 1, 1
        
        for i in range(n - 1):
            temp = one
            one = one + two
            two = temp
            
        return one