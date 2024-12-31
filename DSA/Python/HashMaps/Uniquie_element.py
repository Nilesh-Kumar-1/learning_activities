class Solution:
    def singleNumber(self, nums) -> int:
        result = 0 
        for num in nums: 
            result ^= num 
        return result

# Self-Cancellation:

# a ^ a = 0 for any integer a. When you XOR a number with itself, the result is 0.

# Identity:

# a ^ 0 = a for any integer a. XORing a number with 0 returns the number itself.

# Commutative:

# a ^ b = b ^ a. The order of operands does not matter.

# Associative:

# (a ^ b) ^ c = a ^ (b ^ c). The grouping of operands does not matter.

# Inversion:

# a ^ b ^ b = a. If you XOR a number with another number and then XOR the result with the same number, you get the original number back.