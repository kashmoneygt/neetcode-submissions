class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xffffffff  # Use a mask of 32 ones to fake 32-bit ints in Python

        while b != 0:
            carry = (a & b) << 1  # AND to find carry
            a = (a ^ b) & mask  # XOR
            b = carry & mask  # Let b represent the carry

        # mask // 2 is 31 ones and if a is greater, then its negative
        if a > mask // 2:
            return ~(a ^ mask)
        else:
            return a