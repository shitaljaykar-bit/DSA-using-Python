from collections import Counter

class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        counts = Counter(s)
        
        # Step 1: Split counts into half-frequencies and center character
        half_counts = [0] * 26
        mid_char = ""
        for char, cnt in counts.items():
            idx = ord(char) - ord('a')
            half_counts[idx] = cnt // 2
            if cnt % 2 == 1:
                mid_char = char

        # Helper to compute permutations of remaining counts capped at k
        def count_arrangements(freq_list):
            total = sum(freq_list)
            res = 1
            for freq in freq_list:
                if freq == 0:
                    continue
                # Calculate nCr capped at k
                # Choose 'freq' positions out of 'total'
                r = min(freq, total - freq)
                nCr = 1
                for i in range(1, r + 1):
                    nCr = nCr * (total - i + 1) // i
                    if nCr > k:
                        nCr = k + 1
                        break
                
                res *= nCr
                if res > k:
                    return k + 1
                total -= freq
            return res

        # Step 2: Validate total possible permutations
        total_possible = count_arrangements(half_counts)
        if k > total_possible:
            return ""

        # Step 3: Construct the first half character-by-character
        half_len = sum(half_counts)
        first_half = []

        for _ in range(half_len):
            for i in range(26):
                if half_counts[i] > 0:
                    half_counts[i] -= 1
                    ways = count_arrangements(half_counts)
                    
                    if k <= ways:
                        first_half.append(chr(i + ord('a')))
                        break
                    else:
                        k -= ways
                        half_counts[i] += 1  # Backtrack

        first_half_str = "".join(first_half)
        return first_half_str + mid_char + first_half_str[::-1]
        