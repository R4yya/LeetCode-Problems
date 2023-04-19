class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0 or x == 1:
            return x

        aprox = x

        while x > aprox // x:
            x = (x + aprox // x) // 2

        return x
