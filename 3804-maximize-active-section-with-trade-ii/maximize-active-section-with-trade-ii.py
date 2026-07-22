from typing import List

class SparseTable:
    """Sparse Table for Range Maximum Query in O(1) time complexity."""
    def __init__(self, nums: List[int]):
        self.n = len(nums)
        if self.n == 0:
            return
        K = self.n.bit_length()
        self.st = [[0] * self.n for _ in range(K)]
        self.st[0] = list(nums)
        
        for i in range(1, K):
            for j in range(self.n - (1 << i) + 1):
                self.st[i][j] = max(
                    self.st[i - 1][j], 
                    self.st[i - 1][j + (1 << (i - 1))]
                )

    def query(self, l: int, r: int) -> int:
        if l > r or l < 0 or r >= self.n:
            return 0
        i = (r - l + 1).bit_length() - 1
        return max(self.st[i][l], self.st[i][r - (1 << i) + 1])


class Group:
    def __init__(self, start: int, length: int):
        self.start = start
        self.length = length


class Solution:
    def maxActiveSectionsAfterTrade(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)
        ones = s.count('1')
        
        # 1. Group contiguous '0' blocks and record group index for every position
        zero_groups: List[Group] = []
        zero_group_index: List[int] = []
        
        for i in range(n):
            if s[i] == '0':
                if i > 0 and s[i - 1] == '0':
                    zero_groups[-1].length += 1
                else:
                    zero_groups.append(Group(i, 1))
            # Every position (both '0' and '1') gets mapped to the current zero_groups size - 1
            zero_group_index.append(len(zero_groups) - 1)

        # If there are no zero groups, no trade can be performed
        if not zero_groups:
            return [ones] * len(queries)

        # 2. Build Sparse Table for merged adjacent zero groups
        zero_merge_lengths = [
            zero_groups[i].length + zero_groups[i + 1].length
            for i in range(len(zero_groups) - 1)
        ]
        st = SparseTable(zero_merge_lengths)
        
        ans = []
        
        # 3. Process each query
        for l, r in queries:
            g_l = zero_group_index[l]
            g_r = zero_group_index[r]
            
            left = zero_groups[g_l].length - (l - zero_groups[g_l].start) if g_l != -1 else -1
            right = r - zero_groups[g_r].start + 1 if g_r != -1 else -1
            
            end_group_idx = g_r if s[r] == '1' else g_r - 1
            
            start_adj_idx = g_l + 1
            end_adj_idx = end_group_idx - 1
            
            active_sections = ones
            
            # Case 1: L and R fall into adjacent zero groups
            if s[l] == '0' and s[r] == '0' and g_l + 1 == g_r:
                active_sections = max(active_sections, ones + left + right)
            # Case 2: Max fully contained adjacent pair of zero groups
            elif start_adj_idx <= end_adj_idx:
                active_sections = max(
                    active_sections, 
                    ones + st.query(start_adj_idx, end_adj_idx)
                )
            
            # Case 3: Partial zero group at L + next full zero group
            if s[l] == '0' and g_l + 1 <= end_group_idx:
                active_sections = max(
                    active_sections, 
                    ones + left + zero_groups[g_l + 1].length
                )
            
            # Case 4: Partial zero group at R + previous full zero group
            if s[r] == '0' and g_l < g_r - 1:
                active_sections = max(
                    active_sections, 
                    ones + right + zero_groups[g_r - 1].length
                )
            
            ans.append(active_sections)
            
        return ans