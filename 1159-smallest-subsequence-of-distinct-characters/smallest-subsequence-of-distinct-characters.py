class Solution:
    def smallestSubsequence(self, s: str) -> str:
        # Step 1: Find the last occurrence index of each character
        last_occurrence = {char: i for i, char in enumerate(s)}
        
        stack = []
        seen = set()  # Keeps track of characters currently in the stack
        
        # Step 2: Iterate through the string
        for i, char in enumerate(s):
            # If the character is already in our result stack, skip it
            if char in seen:
                continue
                
            # Maintain monotonic increasing order where possible
            # Pop characters from stack if:
            # 1. The stack is not empty
            # 2. The top of the stack is lexicographically greater than the current char
            # 3. The top character appears again later in the string
            while stack and stack[-1] > char and last_occurrence[stack[-1]] > i:
                removed_char = stack.pop()
                seen.remove(removed_char)
                
            # Push the current character to the stack and mark it as seen
            stack.append(char)
            seen.add(char)
            
        return "".join(stack)