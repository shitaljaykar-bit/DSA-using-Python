class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_map = {}  # Stores the last seen index of each character
        left = 0
        max_length = 0

        for right, char in enumerate(s):
            # If the character is already in the map and within the current window
            if char in char_map and char_map[char] >= left:
                left = char_map[char] + 1  # Move left pointer past the duplicate

            char_map[char] = right  # Update/add character's latest index
            max_length = max(max_length, right - left + 1)  # Track maximum length

        return max_length