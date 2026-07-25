class Solution:
    def maxProduct(self, n: int) -> int:
        # Extract all digits from n as integers
        digits = sorted([int(d) for d in str(n)], reverse=True)
        
        # Multiply the largest two digits
        return digits[0] * digits[1]
        