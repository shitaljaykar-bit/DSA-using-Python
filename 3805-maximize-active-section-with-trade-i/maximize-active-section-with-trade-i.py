class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        initial_ones = s.count('1')
        
        t = '1' + s + '1'
        Z, B = [], []
        
        i = 0
        n = len(t)
        
        # Skip leading '1' block
        while i < n and t[i] == '1':
            i += 1
            
        while i < n:
            # Measure '0' block
            z_start = i
            while i < n and t[i] == '0':
                i += 1
            Z.append(i - z_start)
            
            # Measure inner '1' block
            if i < n:
                b_start = i
                while i < n and t[i] == '1':
                    i += 1
                if i < n: # Exclude trailing '1' block
                    B.append(i - b_start)
                    
        k = len(Z)
        if k < 2:
            return initial_ones
            
        # Prefix and Suffix Max arrays for Z
        pref_max = [0] * k
        pref_max[0] = Z[0]
        for idx in range(1, k):
            pref_max[idx] = max(pref_max[idx - 1], Z[idx])
            
        suff_max = [0] * k
        suff_max[-1] = Z[-1]
        for idx in range(k - 2, -1, -1):
            suff_max[idx] = max(suff_max[idx + 1], Z[idx])
            
        max_gain = 0
        for idx in range(k - 1):
            # Choice 1: Flip the merged zero block
            gain1 = Z[idx] + Z[idx + 1]
            
            # Choice 2: Flip another zero block
            other_max = 0
            if idx > 0:
                other_max = max(other_max, pref_max[idx - 1])
            if idx + 2 < k:
                other_max = max(other_max, suff_max[idx + 2])
                
            gain2 = other_max - B[idx]
            
            max_gain = max(max_gain, gain1, gain2)
            
        return initial_ones + max_gain