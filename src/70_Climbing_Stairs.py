class Solution:
    def climbStairs(self, n: int) -> int:
        prev1 = 1
        prev2 = 1
        curr = 0

        if n == 1:
            return n

        for i in range(2, n + 1):
            curr = prev1 + prev2
            prev1 = prev2
            prev2 = curr

        return curr
