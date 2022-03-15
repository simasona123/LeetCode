class Solution:
    memo = {}
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        if n in self.memo:
            return self.memo[n]
        else:
            self.memo[n] = self.climbStairs(n-2) + self.climbStairs(n-1) 
            return self.memo[n]
## Recursion + Memoization (Dynamic Programming)

class Solution:
    def climbStairs(self, n: int) -> int:
        # Ternyata membuat pola 1,2,3,5,8,13,dst
        a, b= 1, 2
        if n == 1:
            return a
        if n == 2:
            return b
        for _ in range(n-2):
            temp = b
            b = a + temp
            a = temp
        return b
## Pola