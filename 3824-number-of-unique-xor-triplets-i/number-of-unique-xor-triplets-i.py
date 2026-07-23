class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        n = len(nums)
        
        # For n < 3, we cannot choose 3 distinct elements.
        # - n = 1: Output is 1
        # - n = 2: Output is 2
        if n < 3:
            return n
        
        # For n >= 3, all numbers from 0 to 2^(bit_length(n)) - 1 can be generated using XOR.
        # Thus, the number of unique XOR values is 2^(bit_length(n)), which is 1 << n.bit_length().
        return 1 << n.bit_length()
        